from typing import Tuple
from pydantic import BaseModel, Extra
from pathlib import Path


class Config(BaseModel, extra=Extra.ignore):
    max_bet_gold: int = 100000
    sign_gold: Tuple[int, int] = (1, 150)
    russian_path: Path = Path()