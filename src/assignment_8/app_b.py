#!/usr/bin/env python
"""Unit Converter CLI using Click 8.0 features."""

import click  # type: ignore

# Supported units
UNITS = {"km": 1000.0, "hm": 100.0, "dam": 10.0, "m": 1.0, "dm": 0.1, "cm": 0.01, "mm": 0.001}


# Shell completion for unit names
def unit_completion(ctx: click.Context, param: click.Parameter, incomplete: str) -> list[str]:
    """Provide shell completion for unit names."""
    return [unit for unit in UNITS if unit.startswith(incomplete.lower())]


@click.command()
@click.argument("value", type=float)
@click.argument("from_unit", type=click.STRING, shell_complete=unit_completion)
@click.argument("to_unit", type=click.STRING, shell_complete=unit_completion)
def convert(value: float, from_unit: str, to_unit: str) -> None:
    """Convert a numeric value between metric length units.

    Args:
        value: Value to be converted.
        from_unit: The source unit.
        to_unit: The target unit.

    Raises:
        click.BadParameter: When unsupported unit is used.
    """
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit not in UNITS:
        raise click.BadParameter(
            f"Unsupported 'from' unit: {from_unit}.Only metric length units are supported."
        )

    if to_unit not in UNITS:
        raise click.BadParameter(
            f"Unsupported 'to' unit: {to_unit}Only metric length units are supported."
        )

    try:
        converted = (value * UNITS[from_unit]) / UNITS[to_unit]
        click.echo(f"[INFO]: {value} {from_unit} = {converted:.4f} {to_unit}")
    except Exception as err:
        click.echo(f"[ERROR]: Conversion failed due to: {err}")


if __name__ == "__main__":
    convert()  # type: ignore
