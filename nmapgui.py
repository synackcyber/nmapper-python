#NMAP install: pip install python3-nmap
#Ensure nmap is installed locally
from typing import Text
from PyQt5 import QtWidgets
import sys
import os
import nmap3
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'NMAP Host Scanner'
        self.left = 20
        self.top = 20
        self.width = 700
        self.height = 500
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.getText()
    

    #code
    def getText(self):
        text, okPressed = QInputDialog.getText(self, "NMAP","Network or Hostname:", QLineEdit.Normal, "")
        if okPressed and text != '':
           text2 = text
        nmap = nmap3.Nmap()
        version_result = nmap.nmap_version_detection(text2)
        print(version_result)
        print("scan complete, now lets scan the top 1000")
        results = nmap.scan_top_ports(text2)
        print(results)
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Inital Scan Complete. Would you like to export?")
        msgBox.setWindowTitle("Export")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print("Fuck")
        
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
