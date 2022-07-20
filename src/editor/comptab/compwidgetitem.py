"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

from PyQt6.QtWidgets import QTreeWidgetItem, QPushButton, QTreeWidget
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt, QSize
from gm_resources import *

class CompWidgetItem(QTreeWidgetItem):
    """
    Each component listed in the component list is made from 
    this class object. This widget item will standardize attributes
    such as the fonts, icon image size, etc.
    """

    def __init__(self, icon: QIcon,
     parent: QTreeWidgetItem, treeWidget: QTreeWidget, text="Default"):
        """
        Consturctor for a component list item

        :param icon: Icon for the component
        :param parent: Header/category of the item
        :param treeWidget: Main component list widget
        :param text: Description of the component

        :return: none
        """
        super().__init__(parent) # This sets this component to be the subcomponent of the header
        self.role = Qt.ItemDataRole.DisplayRole; # All the items are for displaying
        self.setText(0, text)
        self.setFont(0, QFont("Open Sans Bold", 12))
        if (icon != None):
            self.setIconFile(icon)

    def setIconFile(self, iconFile: str) -> None:
        """
        Sets the icon next to the description

        :param iconFile: icon file location
        """
        icon = QIcon(iconFile)
        self.setIcon(0, icon)
        