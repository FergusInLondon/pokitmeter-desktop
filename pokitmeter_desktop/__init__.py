import signal
import sys

from PyQt5 import QtWidgets

from .main_gui import MainGui

def run():
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    app = QtWidgets.QApplication(sys.argv)
    window = MainGui() # Not entirely sure why the reference is kept?
    app.exec_()
