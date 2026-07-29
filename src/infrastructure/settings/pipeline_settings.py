"""
Pipeline configuration models.
"""

from pydantic import BaseModel, ConfigDict, Field


class PipelineSettings(BaseModel):
    """
    Represents pipeline execution settings.
    """

    model_config = ConfigDict(frozen=True)

    batch_size: int = Field(
        default=1000,
        gt=0,
        description="Number of records processed per batch."
    )

    max_retries: int = Field(
        default=3,
        ge=0,
        description="Maximum retry attempts for recoverable failures."
    )