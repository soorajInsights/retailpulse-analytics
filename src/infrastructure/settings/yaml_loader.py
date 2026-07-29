"""
YAML configuration loader.
"""

from pathlib import Path
from typing import Any

import yaml


class YamlLoader:
    """
    Loads configuration from a YAML file.
    """

    @staticmethod
    def load(file_path: Path) -> dict[str, Any]:
        """
        Load a YAML configuration file.

        Args:
            file_path:
                Path to the YAML file.

        Returns:
            Configuration dictionary.
        """

        with file_path.open(
            mode="r",
            encoding="utf-8"
        ) as file:
            return yaml.safe_load(file)