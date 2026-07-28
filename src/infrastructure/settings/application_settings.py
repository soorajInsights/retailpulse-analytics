"""
Application configuration models.
"""

from pydantic import BaseModel, Field

from domain.enums.environment import Environment


class ApplicationSettings(BaseModel):
    """
    Represents the application configuration.
    """

    name: str = Field(
        ...,
        description="Application name."
    )

    version: str = Field(
        ...,
        description="Application version."
    )

    environment: Environment = Field(
        ...,
        description="Application execution environment."
    )