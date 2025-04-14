"""AI service module for wisegpt."""

from typing import Optional

from litellm import completion

from wisegpt.config import DEFAULT_API_KEY, DEFAULT_MODEL

TOPICS = [
    "life",
    "success",
    "happiness",
    "personal growth",
    "relationships",
    "decision making",
    "learning",
    "life balance",
    "overcoming challenges",
    "time management",
]


def get_advice(question: str, model: Optional[str] = None) -> str:
    """Get advice from the AI model.

    Args:
        question: The question to get advice about
        model: Optional model name. Defaults to environment variable or "gpt-3.5-turbo"

    Returns:
        str: The AI's response
    """
    model = model or DEFAULT_MODEL

    messages = [
        {
            "role": "system",
            "content": """
            You are a wise advisor.
            Provide clear, actionable advice.  Keep it short and concise.
            Focus on practical steps while maintaining a thoughtful, measured tone.
            Do not use special characters, ordered or unordered lists, or other formatting.
            Do not use markdown.
            """,
        },
        {"role": "user", "content": question},
    ]

    response = completion(
        model=model,
        messages=messages,
        temperature=0.7,
        max_tokens=150,
        api_key=DEFAULT_API_KEY,
    )

    return response.choices[0].message.content


def get_proverb(topic: str, model: Optional[str] = None) -> str:
    """Get a proverb from the AI model.

    Args:
        topic: The topic to get a proverb about
        model: Optional model name. Defaults to environment variable or "gpt-3.5-turbo"

    Returns:
        str: The AI's response with a proverb
    """
    model = model or DEFAULT_MODEL

    messages = [
        {
            "role": "system",
            "content": "You are a wise proverb creator. Create concise, memorable proverbs that capture timeless wisdom.",
        },
        {"role": "user", "content": f"Create a proverb about: {topic}"},
    ]

    response = completion(
        model=model, messages=messages, temperature=0.7, max_tokens=100
    )

    return response.choices[0].message.content
