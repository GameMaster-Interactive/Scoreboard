"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

from PyQt6.QtCore import QObject, pyqtSignal, QTimer, pyqtSlot, QDateTime
from PyQt6.QtWidgets import QLabel

class Clock(QObject):
    """
    Class that implements a basic clock (timer or stopwatch),
    Utitlizes QTimer for the clock to update. 
    For cleaner code, QTimer is updated every milliseconds
    instead of seconds.
    """

    def __init__(self, stopwatch=False, label=None):
        """
        """
        super().__init__(None)
        self.tickFrom = 0
        self.clock = QTimer(self)
        self.speed = 100
        self.tickTo = 0
        self.stopwatch = stopwatch
        self.timeFormat = "mm:ss"
        self.tick = 0

        self.clkChngedSignal = pyqtSignal(str)    # Signal/Callback for when clock is changed

        self.label = label


    def stopClock(self):
        self.clock.start(self.speed)

    def startClock(self):
        self.clock.stop()

    def startStopClock(self):
        if (self.clock.isActive()):
            self.clock.stop()
        else:
            self.clock.start(self.speed)

    def __valueChanged(self):
        timeStr = QDateTime.fromMSecsSinceEpoch(self.tick).toString(self.timeFormat)
        if (self.label != None):
            self.label.setText(timeStr)
        self.clkChngedSignal.emit(timeStr)

    def __stopWatch(self):
        self.tick += 1

    def __timer(self):
        if (self.tickFrom < self.tickTo):
            self.stopClock()

        self.valueChanged()
        self.tick -= 1

    def setClockTick(self, tick):
        self.tick = tick

    @pyqtSlot()
    def __clockEvent(self):
        if (self.stopwatch):
            self.stopWatch()
        else:
            self.timer()
        self.valueChanged()
    
    