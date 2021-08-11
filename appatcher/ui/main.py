import os
import shutil
import tempfile
import threading
from pathlib import Path

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (QApplication, QFileDialog, QGridLayout,
                             QHBoxLayout, QLabel, QLineEdit, QMainWindow, QMenu,
                             QPushButton, QTextBrowser, QWidget)

from ..music.player import Player
from ..patcher import patch as p


class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.dirpath = Path(tempfile.mkdtemp())
        self.apk = "/path/to/app.apk"
        self.patch = "/path/to/patch.patch"

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

    def _loadApk(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', str(Path.home()),
                                            "APK File (*.apk *.apks *.xapk)")
        self.apk = Path(fname[0])
        self.inputEdit.setText(str(self.apk))

    def _loadPatch(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', str(Path.home()),
                                            "Diff patch file (*.diff *.patch)")
        self.patch = Path(fname[0])
        self.diffPatchEdit.setText(str(self.patch))

    def _patch(self):
        self.outputTextBrowser.setText("Patching...")
        self.outputTextBrowser.append(
            f"Current temporary dir: {str(self.dirpath)}")

        res, out = p.sanity_checks(self.apk, self.patch)
        if not res:
            self.outputTextBrowser.append(out)
            return

        out, err = p.decompile(self.apk, self.dirpath / "decompiled")
        self.outputTextBrowser.append(out)

        self.outputTextBrowser.append("Applying patch...")
        p.patch(self.patch, root=self.dirpath / "decompiled")

        out, err = p.obfuscate(self.dirpath / "decompiled")
        self.outputTextBrowser.append(out)
        self.outputTextBrowser.append(err)

        out_apk = self.apk.parent / (self.apk.stem + "_patched.apk")
        out, err = p.recompile(src=self.dirpath / "decompiled", apk=out_apk)
        self.outputTextBrowser.append(out)

        out, err = p.sign(apk=out_apk, dst=self.apk.parent)
        self.outputTextBrowser.append(out)

        self.outputTextBrowser.append(
            f"Patched and Signed APK at: {str(out_apk.parent)}")

    def mainGrid(self) -> QGridLayout:
        inputButton = QPushButton('Load APK', self)
        inputButton.clicked.connect(self._loadApk)
        diffPatchButton = QPushButton('Load Patch', self)
        diffPatchButton.clicked.connect(self._loadPatch)
        outputLabel = QLabel('Output')

        self.inputEdit = QLabel('No APK selected...')
        self.diffPatchEdit = QLabel('No patch selected...')
        self.outputTextBrowser = QTextBrowser()

        patchButton = QPushButton('Patch APK', self)
        patchButton.clicked.connect(self._patch)
        cancelButton = QPushButton('Cancel', self)
        cancelButton.clicked.connect(QApplication.instance().quit)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(inputButton, 1, 0)
        grid.addWidget(self.inputEdit, 1, 1)

        grid.addWidget(diffPatchButton, 2, 0)
        grid.addWidget(self.diffPatchEdit, 2, 1)

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
        shutil.rmtree(self.dirpath)

        return super().closeEvent(event)
