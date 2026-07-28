"""
Data storage configuration models.
"""

from pathlib import Path

from pydantic import BaseModel, ConfigDict, Field


class DataStorageSettings(BaseModel):
    """
    Represents data storage locations.
    """

    model_config = ConfigDict(frozen=True)

    raw_path: Path = Field(
        ...,
        description="Path to the raw data directory."
    )

    bronze_path: Path = Field(
        ...,
        description="Path to the bronze layer."
    )

    silver_path: Path = Field(
        ...,
        description="Path to the silver layer."
    )

    gold_path: Path = Field(
        ...,
        description="Path to the gold layer."
    )

    generated_path: Path = Field(
        ...,
        description="Path to generated datasets."
    )