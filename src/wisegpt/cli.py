"""Main CLI module for wisegpt."""

from typing import Optional

import click

from wisegpt.ai_service import get_advice


@click.command()
@click.argument("question", required=False)
@click.option("--model", "-m", help="AI model to use")
def ask(question: Optional[str] = None, model: Optional[str] = None) -> None:
    """Ask wisegpt for advice or wisdom.

    Args:
        question: The question or topic to get advice about.
        model: Optional model name to use.
    """
    if question is None:
        question = click.prompt("What would you like advice about?")

    with click.progressbar([1], label="Thinking...", show_eta=False) as bar:
        for _ in bar:
            advice = get_advice(question, model)

    click.echo(f"\n{advice}")


def main() -> None:
    """Entry point for the CLI application."""
    ask()
