"""Command-line interface for test_python."""

import typer

from test_python import __version__

app = typer.Typer(
    name="test_python",
    help="A Python package",
    add_completion=False,
)


def version_callback(value: bool) -> None:
    """Print version and exit."""
    if value:
        typer.echo(f"test_python version: {__version__}")
        raise typer.Exit


@app.callback()
def main(
    version: bool | None = typer.Option(
        None,
        "--version",
        "-v",
        help="Show version and exit.",
        callback=version_callback,
        is_eager=True,
    ),
) -> None:
    """A Python package."""


@app.command()
def hello(
    name: str = typer.Argument("World", help="Name to greet"),
) -> None:
    """Say hello to someone."""
    typer.echo(f"Hello, {name}!")


if __name__ == "__main__":
    app()
