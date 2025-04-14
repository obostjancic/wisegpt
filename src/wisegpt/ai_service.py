"""AI service module for wisegpt."""

import os
from typing import Optional

from litellm import completion


def get_advice(question: str, model: Optional[str] = None) -> str:
    """Get advice from the AI model.

    Args:
        question: The question to get advice about
        model: Optional model name. Defaults to environment variable or "gpt-3.5-turbo"

    Returns:
        str: The AI's response
    """
    model = model or os.getenv("WISEGPT_MODEL", "gpt-3.5-turbo")

    messages = [
        {
            "role": "system",
            "content": "You are a wise advisor. Provide concise, practical advice.",
        },
        {"role": "user", "content": question},
    ]

    response = completion(
        model=model, messages=messages, temperature=0.7, max_tokens=150
    )

    return response.choices[0].message.content
