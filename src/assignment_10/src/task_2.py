"""Script demonstrating the CLI execution using multithreading."""

import concurrent.futures as cf
import functools
import threading
import time

import click
from src.task_1 import log_execution_time  # type: ignore


def log_thread_lifecycle(func):
    """Display the time taken for the thread to complete the execution.

    Args:
        func: The function to be timed.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper to time the thread execution."""
        thread_name = threading.current_thread().name
        start_time = time.perf_counter()
        click.echo(f"[START] Thread {thread_name}")
        result = func(*args, **kwargs)
        click.echo(f"[END] Thread {thread_name}")
        end_time = time.perf_counter()
        click.echo(f"Elapsed time {thread_name}: {(end_time - start_time)*100 :.4f} ms.")
        return result

    return wrapper


@log_thread_lifecycle
def echo_word_helper(statement: str) -> str:
    """Helper function to time the threads."""
    return statement


def echo_message_implementation(count: int, message: str) -> None:
    """Function implementation of `echo_message`."""
    if count <= 0:
        raise click.BadParameter("Count must be greater than 0.")
    with cf.ThreadPoolExecutor(max_workers=count) as executor:
        results = [executor.submit(echo_word_helper, f"{i+1}. {message}") for i in range(count)]

        for f in cf.as_completed(results):
            click.echo(f.result())


@log_execution_time
@click.command(
    help="""Examples:\n
        $ python task_1.py -c 3 HelloWorld\n
        $ python task_1.py --count 3 "Hello World"\n"""
)
@click.option(
    "--count", "-c", type=int, default=1, help="Number of times the words must be printed."
)
@click.argument("message", type=str)
@click.help_option("-h", "--help", help="To show the help message.")
def echo_message(count: int, message: str) -> None:
    """CLI command to display the message `count` times on the console.

    Args:
        count: Number of times the message has to be displayed.
        message: The message to be displayed.

    Raises:
        click.BadParameter: Raised when the count is less than 0.
    """
    echo_message_implementation(count, message)


if __name__ == "__main__":
    echo_message()
