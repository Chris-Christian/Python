import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):       

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first GUI")
        self.setGeometry(450,150,500,500)
        label=QLabel("Hello",self)
        label.setFont(QFont("Arial",40))
        label.setGeometry(0,0,500,100)
        label.setStyleSheet("color: #0a0a09;"
                            "background-color: #a4aff5;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        #label.setAlignment(Qt.AlignTop)                     
        #label.setAlignment(Qt.AlignVCenter)                    Vertical center
        #label.setAlignment(Qt.AlignHCenter)                    Horizontal center
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  Vertical and horizontal center
        label.setAlignment(Qt.AlignCenter)

def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())          

if __name__=="__main__":
    main()