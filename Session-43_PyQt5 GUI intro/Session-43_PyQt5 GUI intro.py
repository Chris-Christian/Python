import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
# QApplication → Manages the whole app (event loop, windows, etc.)
# QMainWindow → A ready-made window class with menu bar, title bar, status bar, etc.
# QIcon → used to set the window's icon.

class MainWindow(QMainWindow):          #Defines a new class called MainWindow, which inherits from PyQt's built-in QMainWindow.
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first GUI")
        self.setGeometry(450,150,500,500)
        self.setWindowIcon(QIcon("nature.jpg"))

def main():
    app=QApplication(sys.argv)          #sys.argv allows passing command-line options
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())               #app.exec_() keeps running until the window is closed.

if __name__=="__main__":
    main()
