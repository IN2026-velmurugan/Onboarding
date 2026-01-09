"""Script demonstrating the cli command."""

import time

import click


def log_execution_time(func):
    """Display the time taken by the wrapper function.

    Args:
        func: The function to be timed.
    """

    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        click.echo(f"Elapsed time : {(end_time - start_time)*100 :.4f} ms.")

    return wrapper


@click.command()
@click.option("--count", default=1, help="Number of times the words must be printed.")
@click.argument("message")
@log_execution_time
def echo_message(count, message) -> None:
    """CLI command to display the message `count` times on the console.

    Args:
        count: Number of times the message has to be displayed.
        message: The message to be displayed.

    Raises:
        click.BadParameter: Raised when the count is less than 0.
    """
    if count <= 0:
        raise click.BadParameter("Count must be greater than 0.")

    for i in range(count):
        click.echo(f"{i+1}. {message}")


if __name__ == "__main__":
    echo_message()
