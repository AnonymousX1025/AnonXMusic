# Copyright (c) 2025 AnonymousX1025
# Licensed under the MIT License.
# This file is part of AnonXMusic


from pathlib import Path

from anony import logger


def ensure_dirs():
    """
    Ensure that the necessary directories exist.
    """
    for dir in ["cache", "downloads"]:
        Path(dir).mkdir(parents=True, exist_ok=True)
    logger.info("Cache directories updated.")
