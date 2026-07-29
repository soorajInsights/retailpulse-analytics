"""
Snowflake configuration models.
"""

from pydantic import BaseModel, ConfigDict, Field


class SnowflakeSettings(BaseModel):
    """
    Represents Snowflake connection settings.
    """

    model_config = ConfigDict(frozen=True)

    account: str = Field(
        ...,
        description="Snowflake account identifier."
    )

    user: str = Field(
        ...,
        description="Snowflake username."
    )

    password: str = Field(
        ...,
        description="Snowflake password."
    )

    warehouse: str = Field(
        ...,
        description="Snowflake warehouse."
    )

    database: str = Field(
        ...,
        description="Snowflake database."
    )

    schema: str = Field(
        ...,
        description="Snowflake schema."
    )

    role: str = Field(
        ...,
        description="Snowflake role."
    )