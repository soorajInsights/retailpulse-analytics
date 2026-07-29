"""
Logging configuration models.
"""

from pathlib import Path

from pydantic import BaseModel, ConfigDict, Field


class LoggingSettings(BaseModel):
    """
    Represents logging configuration.
    """

    model_config = ConfigDict(frozen=True)

    level: str = Field(
        ...,
        description="Logging level."
    )

    file: Path = Field(
        ...,
        description="Log file path."
    )

    console: bool = Field(
        default=True,
        description="Enable console logging."
    )

    rotation: str = Field(
        default="10 MB",
        description="Maximum log file size before rotation."
    )

    retention: str = Field(
        default="7 days",
        description="Retention period for log files."
    )