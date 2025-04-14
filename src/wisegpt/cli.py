"""Main CLI module for wisegpt."""

import random
from typing import Optional

import click

from wisegpt.ai_service import TOPICS, get_advice, get_proverb
from wisegpt.config import AVAILABLE_MODELS, DEFAULT_MODEL
from wisegpt.monitoring import init_monitoring


@click.group()
def cli() -> None:
    """WiseGPT - Your AI Wisdom Companion."""


@cli.command()
@click.argument("question", required=False)
@click.option(
    "--model",
    "-m",
    type=click.Choice(AVAILABLE_MODELS, case_sensitive=False),
    default=DEFAULT_MODEL,
    help="AI model to use",
)
def advice(question: Optional[str] = None, model: Optional[str] = None) -> None:
    """Ask wisegpt for advice or wisdom.

    Args:
        question: The question or topic to get advice about.
        model: Optional model name to use.
    """
    advice_text = ""
    if question is None:
        prompt = random.choice(TOPICS)
        advice_text = get_advice(prompt, model)
        click.echo(prompt)
    else:
        with click.progressbar(
            [1], label="Thinking...", show_eta=False
        ) as progress_bar:
            for _ in progress_bar:
                advice_text = get_advice(question, model)

    click.echo(f"\n{advice_text}")


@cli.command()
@click.argument("topic", required=False)
@click.option(
    "--model",
    "-m",
    type=click.Choice(AVAILABLE_MODELS, case_sensitive=False),
    default=DEFAULT_MODEL,
    help="AI model to use",
)
def proverb(topic: Optional[str] = None, model: Optional[str] = None) -> None:
    """Get a proverb from wisegpt.

    Args:
        topic: The topic to get a proverb about.
        model: Optional model name to use.
    """
    proverb_text = ""
    if topic is None:
        prompt = random.choice(TOPICS)
        proverb_text = get_proverb(prompt, model)
    else:
        with click.progressbar(
            [1], label="Creating proverb...", show_eta=False
        ) as progress_bar:
            for _ in progress_bar:
                proverb_text = get_proverb(topic, model)

    click.echo(f"\n{proverb_text}")


@cli.command()
def models() -> None:
    """List available models."""
    click.echo("Available models:")
    for model in AVAILABLE_MODELS:
        if model == DEFAULT_MODEL:
            click.echo(f"  {model} (default)")
        else:
            click.echo(f"  {model}")


def main() -> None:
    """Entry point for the CLI application."""
    init_monitoring()
    cli()
