"""Script to define the command for displaying the messages using grpc or local."""

import click

from .task_2 import echo_message_implementation
from .task_3 import repeat_message_grpc


@click.command
@click.option("--message", type=str, default="!!!", help="Message to be repeated.")
@click.option("--count", type=int, default=1, help="Number of times the words must be printed.")
@click.option("--use-grpc", is_flag=True, help="Sends the message and count to the gRPC server.")
def repeat_message(count: int, message: str, use_grpc: bool):
    """CLI command to display the message `count` times on the console using grpc or local.

    Args:
        count: Number of times the message has to be displayed.
        message: The message to be displayed.
        use_grpc: Flag, when set runs the grpc function.

    Raises:
        click.BadParameter: Raised when the count is less than 0.
    """
    if count <= 0:
        raise click.BadParameter("Count must be greater than 0.")
    if use_grpc:
        click.echo("Sending the request to gRPC.")
        repeat_message_grpc(count, message)
    else:
        click.echo("executing as normal program")
        echo_message_implementation(count, message)


if __name__ == "__main__":
    repeat_message()
