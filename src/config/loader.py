from __future__ import annotations
import json

from src.config.parser import Parser
from src.config.schema import Config
from src.utils.exceptions import ConfigError


def load_config(path: str) -> Config:
    """Load, validate, and type a config file.

    Raises:
        ConfigError: file missing/unreadable, or not valid JSON.
    """
    try:
        raw = Parser(path).parse()
    except FileNotFoundError as exc:
        raise ConfigError(f"configuration file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ConfigError(f"invalid JSON in '{path}': {exc}") from exc
    except OSError as exc:
        raise ConfigError(f"could not read config "
                          f"file '{path}': {exc}") from exc

    return Config.from_dict(raw)
