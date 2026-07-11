from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class MenubarCascade:
    label: str
    menu: Any
    underline: int = 0
