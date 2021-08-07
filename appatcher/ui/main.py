import threading

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
                             QLineEdit, QMainWindow, QMenu, QPushButton,
                             QTextBrowser, QWidget)

from ..music.player import Player


class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        wid = QWidget(self)
        self.setCentralWidget(wid)

        self.setupMenuBar()
        grid = self.mainGrid()

        wid.setLayout(grid)

        self.resize(350, 250)
        self.center()
        self.setWindowTitle('Appatcher v0.0.1')

        self.show()

        self.player = Player()
        self.musicThread = threading.Thread(target=self.player.run)
        self.musicThread.start()

    def switchMusic(self):
        if self.player.isRunning():
            self.player.terminate()
        else:
            self.musicThread = threading.Thread(target=self.player.run)
            self.musicThread.start()

    def setupMenuBar(self) -> None:
        menubar = self.menuBar()
        # Запускать и останавливать музыку
        musicMenu = menubar.addMenu('Music')
        playAct = QAction('Play/Pause', self)
        musicMenu.addAction(playAct)
        playAct.triggered.connect(self.switchMusic)

        # Другие инструменты для взлома
        extraMenu = menubar.addMenu('Extra Tools')

        sapMenu = QMenu('Split APK Patcher', self)
        sapDownloadAct = QAction('Download', self)
        sapVisitAct = QAction('Visit Website', self)
        sapMenu.addAction(sapDownloadAct)
        sapMenu.addAction(sapVisitAct)
        extraMenu.addMenu(sapMenu)

        smobMenu = QMenu('Smob - Obfuscation tool', self)
        smobDownloadAct = QAction('Download', self)
        smobVisitAct = QAction('Visit Website', self)
        smobMenu.addAction(smobDownloadAct)
        smobMenu.addAction(smobVisitAct)
        extraMenu.addMenu(smobMenu)

        # Обо мне)
        aboutMenu = menubar.addMenu('About')

    def mainGrid(self) -> QGridLayout:
        inputButton = QPushButton('Load APK', self)
        diffPatchButton = QPushButton('Load Patch', self)
        outputLabel = QLabel('Output')

        inputEdit = QLineEdit('Input APK')
        diffPatchEdit = QLineEdit('Patch')
        self.outputTextBrowser = QTextBrowser()

        patchButton = QPushButton('Patch APK', self)
        cancelButton = QPushButton('Cancel', self)
        cancelButton.clicked.connect(QApplication.instance().quit)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(inputButton, 1, 0)
        grid.addWidget(inputEdit, 1, 1)

        grid.addWidget(diffPatchButton, 2, 0)
        grid.addWidget(diffPatchEdit, 2, 1)

        grid.addWidget(outputLabel, 3, 0)
        grid.addWidget(self.outputTextBrowser, 3, 1)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(patchButton)
        hbox.addWidget(cancelButton)

        grid.addLayout(hbox, 4, 1)

        return grid

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event) -> None:
        self.player.terminate()

        return super().closeEvent(event)
