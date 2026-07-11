from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class MenubarCommand:
    label: str
    command: Callable