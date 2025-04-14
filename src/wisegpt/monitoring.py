"""Monitoring and error tracking for wisegpt."""

import os
from typing import Optional

import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration

from wisegpt.config import DEFAULT_MODEL


def init_monitoring(dsn: Optional[str] = None) -> None:
    """Initialize monitoring and error tracking.

    Args:
        dsn: Optional Sentry DSN. If not provided, uses WISEGPT_SENTRY_DSN env var.
    """
    dsn = dsn or os.getenv("WISEGPT_SENTRY_DSN")
    if not dsn:
        return

    sentry_sdk.init(
        dsn=dsn,
        traces_sample_rate=1.0,
        profiles_sample_rate=1.0,
        environment=os.getenv("WISEGPT_ENV", "development"),
        integrations=[
            LoggingIntegration(
                level=20,  # INFO
                event_level=40,  # ERROR
            ),
        ],
    )

    sentry_sdk.set_tag("default_model", DEFAULT_MODEL)
