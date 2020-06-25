from pathlib import Path
from tkinter import (
    Tk,
    Frame,
    Button,
    Canvas,
    X,
    RIGHT,
    BOTH,
)

from GUISettings import GUISettings

gui = GUISettings()
class ExcelBox(Tk):

    def __init__(
            self,
            title: str = 'Excelbox',
            color: str = gui.bg_color,
            geometry: str = gui.geo,
            photo_path: str = str(Path.cwd() / 'images' / 'excel_icon.png')
        ):
        
        super().__init__()
        self.iconphoto(False, photo_path)
        self.title(title)
        self.configure(background=color)
        self.geometry(geometry)

        self.mainloop()

    @classmethod
    def custombox(
            cls,
            title: str = None,
            color: str = None,
            geometry: str = None,
        ):
        return cls(title, color, geometry)

    # @staticmethod
    # def trialbox():
    #     root=Tk()
    #     def move_window(event): geometry(f'+{event.x_root}+{event.y_root}')

    #     # reconfigure title bar
    #     overrideredirect(True)
    #     title_bar = Frame(self, bg='dark green')
    #     close_btn = Button(title_bar, text='X', command=destroy)
        

    #     window = Canvas(self, bg=color)
        
    #     title_bar.pack(expand=1, fill=X)
    #     close_btn.pack(side=RIGHT)
    #     window.pack(expand=1, fill=BOTH)
        
    #     title_bar.bind('<B1-Motion>', move_window)

a = ExcelBox()
        