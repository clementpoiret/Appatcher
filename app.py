import sys
from PyQt6.QtWidgets import QApplication

from appatcher.ui.main import MainWindow


def main():
    app = QApplication(sys.argv)
    ex = MainWindow()

    ex.outputTextBrowser.append('Hello World')

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
