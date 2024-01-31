import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, QUrl, QDir, QFileInfo
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QToolBar, QPushButton, QLineEdit, QStyleFactory, QLineEdit, QFileDialog, QMessageBox, QFileDialog, QAction
#from PyQt5.QtCore import pyQtSlot
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView, QWebEngineSettings, QWebEngineDownloadItem
from PyQt5 import uic
from pathlib import Path
import sqlite3

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class WebEnginePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.img0 = "./48.png"
        self.setGeometry(100, 100, 900, 600)
        self.setWindowTitle("Cooltebza")
        self.setWindowIcon(QIcon(resource_path(self.img0)))
        self.view = QWebEngineView()
        self.page = QWebEnginePage(self.view)
        self.view.setPage(self.page)
        self.path = QDir.current().filePath(resource_path("index.html"))
        self.view.load(QUrl.fromLocalFile(self.path))
        self.setCentralWidget(self.view)

        self.channel = QWebChannel()
        self.channel.registerObject('backend', self)
        self.view.page().setWebChannel(self.channel)
        self.view.show()
        
        self.view.page().settings().setAttribute(QWebEngineSettings.LocalStorageEnabled, True)
        self.view.page().settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.view.page().titleChanged.connect(self.getTitles)
        self.view.page().profile().downloadRequested.connect(self.on_downloadRequested)
       
        #QMenu *viewMenu = menuBar().addMenu(tr("&View"));
        #QAction *viewSourceAction = new QAction(tr("Page Source"), this);
        #connect(viewSourceAction, &QAction::triggered, this, &MainWindow::viewSource);
        #viewMenu.addAction(viewSourceAction);
        self.access = ["id","key","access"]
        self.access = ["id","uname","upwd"]


    @pyqtSlot(str)
    def getTitle(self, title):
        self.setWindowTitle(title)
    
    def getTitles(self, title):
        m = self.view.page().title()
        self.setWindowTitle(m)

    @pyqtSlot(QAction)
    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save Page As", "",
                        "Hypertext Markup Language (*.htm *html);;"
                        "All files (*.*)")

        if filename:
            html = self.browser.page().toHtml()
            with open(filename, 'w') as f:
                f.write(html)

    @pyqtSlot(QWebEngineDownloadItem)
    def on_downloadRequested(self, download):
        old_path = download.path()
        suffix = QFileInfo(old_path).suffix()
        path,_ = QFileDialog.getSaveFileName(self.view,  "Save File",
        old_path, "*."+suffix)
        if path:
            download.setPath(QDir(path))
            download.accept()
       
if __name__ == '__main__':
    sys.argv.append("--remote-debugging-port=8000")
    sys.argv.append("--disable-web-security")
    app = QtWidgets.QApplication(sys.argv)
    app.setOrganizationName("Cooltebza Ltd.")
    app.setOrganizationDomain("https://cooltebza.github.io")
    app.setApplicationName("Cooltebza")

    win = WebEnginePage()
    win.show()
    sys.exit(app.exec_())

    
   
