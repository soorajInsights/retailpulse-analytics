"""
Root configuration model.
"""

from pydantic import BaseModel, ConfigDict

from infrastructure.settings.application_settings import ApplicationSettings
from infrastructure.settings.data_storage_settings import DataStorageSettings
from infrastructure.settings.logging_settings import LoggingSettings
from infrastructure.settings.pipeline_settings import PipelineSettings
from infrastructure.settings.snowflake_settings import SnowflakeSettings


class Settings(BaseModel):
    """
    Root application configuration.
    """

    model_config = ConfigDict(frozen=True)

    application: ApplicationSettings
    data: DataStorageSettings
    logging: LoggingSettings
    pipeline: PipelineSettings
    snowflake: SnowflakeSettings