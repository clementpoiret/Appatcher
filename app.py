import subprocess
import sys

from PyQt6.QtWidgets import QApplication

from appatcher.ui.main import MainWindow


def main():
    app = QApplication(sys.argv)
    app.setStyle('Windows')
    ex = MainWindow()

    ex.outputTextBrowser.append("Welcome, and happy patching :)")

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
