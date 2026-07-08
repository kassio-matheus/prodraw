from dataclasses import dataclass


@dataclass
class Window():
    """Abstract base class representing a generic window screen."""

    title: str
    is_fullscreen: bool = True
    width: int = 800
    height: int = 600