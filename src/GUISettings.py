from pathlib import Path
from dataclasses import dataclass
from typing import (
    Tuple,
)


@dataclass
class GUISettings:

    # general settings
    file_dir: Path = Path(__file__).parents[0]
    bg_color: str = 'gray88'
    font_color: str = 'white'
    geo: str = '300x180'

    # dropdown settings
    drop_x: int = 63

    # button settings
    btn_wid: int = 10
    btn_xy: Tuple[int] = (50, 140)

    # label settings
    lbl_hiwid: Tuple = (55, 170)
    robo_font: Tuple[str, int] = ('Roboto', 10)
    lbl_relief: str = 'groove'
