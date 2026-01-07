"""Script to demonstrate the use of click 7.0."""

import click  # type: ignore


@click.command()
@click.option("--name", prompt="Your name")
def hello(name: str) -> None:
    """Print a greeting to console.

    Args:
        name: Name to greet.
    """
    click.echo(f"Hello {name}")


if __name__ == "__main__":
    hello()  # type: ignore
