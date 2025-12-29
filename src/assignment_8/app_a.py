"""Script to demonstrate the use of click 7.0."""

import click  # type: ignore


@click.command()
@click.option("--name", prompt="Your name")
def hello(name: str) -> None:
    """Display the string in the console.

    Args:
        name: Content to be displayed.
    """
    click.echo(f"Hello {name}")


if __name__ == "__main__":
    hello()  # type: ignore
