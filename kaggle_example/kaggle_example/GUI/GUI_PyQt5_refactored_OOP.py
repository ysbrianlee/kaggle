import sys
from PyQt5.QtWidgets import QApplication, QWidget

class GUI(QWidget):
    def __init__(self):
        super().__init__()
        # 윈도우를 생성하고 슈퍼클래스를 초기화
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt5 GUI')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())
