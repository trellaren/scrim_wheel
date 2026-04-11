import random
from typing import List

import typer

app = typer.Typer(help="Randomly roll items from a list.")


@app.command()
def roll(
    items: List[str] = typer.Argument(..., help="Items to roll from."),
    count: int = typer.Option(1, "--count", "-n", help="Number of items to select.", min=1),
) -> None:
    """Randomly select count items from items."""
    if count > len(items):
        typer.echo(
            f"Error: count ({count}) cannot exceed the number of items ({len(items)}).",
            err=True,
        )
        raise typer.Exit(code=1)

    selected = random.sample(items, count)
    for item in selected:
        typer.echo(item)


if __name__ == "__main__":
    app()
