"""Script to define the command for displaying the messages using grpc or local."""

import click
from src.task_2 import echo_message_implementation  # type: ignore
from src.task_3.message_client import repeat_message_grpc  # type: ignore


@click.command(
    help="""Examples:\n
        $ python task_1.py --count 3 --message HelloWorld\n
        $ python task_1.py --count 3 --message "Hello World"\n"""
)
@click.option(
    "--message",
    type=str,
    default="!!!",
    help="Message to be repeated. Use double quotes on Windows if the message contains spaces.",
)
@click.option("--count", type=int, default=1, help="Number of times the words must be printed.")
@click.option(
    "--use-grpc", is_flag=True, type=bool, help="Sends the message and count to the gRPC server."
)
@click.help_option("-h", "--help", help="To show the help message.")
def repeat_message(count: int, message: str, use_grpc: bool) -> None:
    """CLI command to display the message `count` times on the console using grpc or local.

    Args:
        count: Number of times the message has to be displayed.
        message: The message to be displayed.
        use_grpc: Flag, when set runs the grpc function.

    Raises:
        click.BadParameter: Raised when the count is less than 0.
    """
    try:
        if count <= 0:
            raise click.BadParameter("Count must be greater than 0.")
        if use_grpc:
            click.echo("Sending the request to gRPC.")
            repeat_message_grpc(count, message)
        else:
            click.echo("Executing as normal program")
            echo_message_implementation(count, message)
    except click.ClickException:
        raise

    except Exception as e:
        raise click.ClickException(str(e))


if __name__ == "__main__":
    repeat_message()
