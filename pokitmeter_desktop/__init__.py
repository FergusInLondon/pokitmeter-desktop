import sys

from PyQt5 import QtWidgets

from .main_gui import MainGui


def run():
    app = QtWidgets.QApplication(sys.argv)
    window = MainGui() # Not entirely sure why the reference is kept?
    app.exec_()
