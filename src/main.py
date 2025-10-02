"""Test module."""

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def greet(name: str) -> str:
    """Greet the user with a message."""
    return f"Hello, {name}!"


def main() -> None:
    """Test function."""
    logger.info(greet("World"))


if __name__ == "__main__":
    main()
