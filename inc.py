import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from pathlib import Path
import sqlite3

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

companyName = "Cooltebza"
companyDomain = "https://cooltebza.github.io"
companyIcon = ":/48.png"

fontNum = "0"
def fontStyle():
    font = QtGui.QFont()
    font.setFamily("Sitka")
    font.setPointSize(12)
    font.setBold(True)
    font.setWeight(75)
    #winFont.setFont(font)
    
