from tkinter import Tk

from GUISettings import GUISettings

gui = GUISettings()
class ExcelBox(Tk):

    def __init__(self):
        super().__init__()

        self.title('ExcelBox')
        self.configure(background=gui.bg_color)
        self.geometry(gui.geo)
        self.mainloop()    
