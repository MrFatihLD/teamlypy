from typing import Any, Union
import logging
from colorama import init, Fore

class _MissingSentinel:
    __slots__ = ()

    def __eq__(self, other) -> bool:
        return False

    def __bool__(self) -> bool:
        return False

    def __hash__(self) -> int:
        return 0

    def __repr__(self):
        return '...'
    
MISSING: Any = _MissingSentinel()

TwoType = Union[str,int]


LEVEL_COLOR = {
    "DEBUG": Fore.LIGHTBLACK_EX,
    "INFO": Fore.BLUE,
    "WARNING": Fore.YELLOW,
    "ERROR": Fore.MAGENTA,
    "CRITICAL": Fore.RED
}

init(autoreset=True)
class FormatLogging(logging.Formatter):
    
    def format(self, record):
        level_color = LEVEL_COLOR.get(record.levelname,"")
        record.levelname = f"{level_color} {record.levelname}"
        return super().format(record)
    
