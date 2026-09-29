class PacmanError(Exception):
    """Base class for all handled errors in this project."""


class ConfigError(PacmanError):
    """Raised when the config file is missing, malformed, or invalid."""
