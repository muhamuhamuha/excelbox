from pathlib import Path
from tkinter import (
    Tk,
    Frame,
    Button,
    Canvas,
    X,
    RIGHT,
    BOTH,
    PhotoImage,
)

from GUISettings import GUISettings

gui = GUISettings()
class ExcelBox(Tk):

    def __init__(
            self,
            title: str = 'ExcelBox',
            color: str = gui.bg_color,
            geometry: str = gui.geo,
            photo_path: str = str(
                Path.cwd() / 'src' / 'images' / 'excel_icon.png'
            )
        ):
        
        super().__init__()
        self.title(title)
        self.configure(background=color)
        self.tk.call(
            'wm',
            'iconphoto',
            self._w,
            PhotoImage(file=photo_path)
        )
        self.geometry(geometry)

        self.mainloop()

    @classmethod
    def custombox(
            cls,
            title: str = None,
            color: str = None,
            geometry: str = None,
            photo_path: str = None,
        ):
        return cls(title, color, geometry)