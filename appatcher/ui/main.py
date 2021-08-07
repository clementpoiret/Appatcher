from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenu, QPushButton


class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        menubar = self.menuBar()

        # Запускать и останавливать музыку
        musicMenu = menubar.addMenu('Music')
        playAct = QAction('Play/Pause', self)
        musicMenu.addAction(playAct)

        extraMenu = menubar.addMenu('Extra Tools')

        sapMenu = QMenu('Split APK Patcher', self)
        sapDownloadAct = QAction('Download', self)
        sapVisitAct = QAction('Visit Website', self)
        sapMenu.addAction(sapDownloadAct)
        sapMenu.addAction(sapVisitAct)
        extraMenu.addMenu(sapMenu)

        aboutMenu = menubar.addMenu('About')

        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        self.resize(350, 250)
        self.center()
        self.setWindowTitle('Appatcher v0.0.1')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())
