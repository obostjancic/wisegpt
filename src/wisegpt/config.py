"""Configuration management for wisegpt."""

import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path(__file__).parent.parent.parent / ".env"
load_dotenv(env_path)

DEFAULT_MODEL = os.getenv("WISEGPT_MODEL", "gpt-3.5-turbo")

AVAILABLE_MODELS = [
    "gpt-3.5-turbo",
    "gpt-4",
    "gpt-4-turbo",
    "gpt-4o-mini",
    "gpt-4o",
    "gemini-pro",
    "gemini-pro-vision",
]

DEFAULT_API_KEY = os.getenv("OPENAI_API_KEY")
