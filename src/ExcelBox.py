from tkinter import Tk

from GUISettings import GUISettings

gui = GUISettings()
class ExcelBox(Tk):

    def __init__(
            self,
            title: str = None,
            color: str = None,
            geometry: str = None,
        ):
        
        super().__init__()
        self.title('ExcelBox' if title is None else title)
        self.configure(
            background=gui.bg_color if color is None else color,
            highlightbackground='dark green',
        )
        self.geometry(gui.geo if geometry is None else geometry)
        self.mainloop()

    @classmethod
    def custombox(
            cls,
            title: str = None,
            color: str = None,
            geometry: str = None,
        ):
        return cls(title, color, geometry)

a = ExcelBox()
