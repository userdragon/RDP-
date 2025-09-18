# src/slave.py
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from core.common.logger import logger

class SlaveWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("同步远程控制 - 被控端")
        self.setGeometry(100, 100, 800, 600)
        self.label = QLabel("被控端运行中...", self)
        self.label.setGeometry(50, 50, 300, 30)

if __name__ == "__main__":
    logger.info("被控端启动")
    app = QApplication([])
    window = SlaveWindow()
    window.show()
    app.exec_()
