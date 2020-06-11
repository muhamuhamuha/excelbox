from pathlib import Path

from tkinter.tkk import (
    Combobox,
)
from tkinter import (
    Tk,
    Button,
    Label,
    StringVar,
    PhotoImage,
    LabelFrame,
)

from GUISettings import GUISettings

gui = GUISettings()
class ExcelBox(Tk):

    def __init__(self):
        super().__init__()

        self.title('ExcelBox')
        self.configure(background=gui.bg_color)
