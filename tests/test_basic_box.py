import unittest

from src.ExcelBox import ExcelBox
from src.GUISettings import GUISettings

class ExcelBoxTest(unittest.TestCase):

    def setUp(self):
        self.box = ExcelBox()
        self.gui = GUISettings()

    def test_default_excelbox_size(self):
        self.assertEqual(self.box.geometry == self.gui.geo)



if __name__ == '__main__':
    unittest.main()