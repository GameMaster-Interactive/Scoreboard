import os

from PyQt6 import QtWidgets, uic
from pathlib import Path

class StartMenu(QtWidgets.QWidget):
    def __init__(self, *args):
        super().__init__(*args) # Call the inherited classes __init__ method
        path = os.fspath(Path(__file__).resolve().parent / "ui/startmenu.ui")
        uic.loadUi(path, self) # Load the .ui file
