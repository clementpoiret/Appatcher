import subprocess
import sys

from PyQt6.QtWidgets import QApplication

from appatcher.ui.main import MainWindow


def main():
    app = QApplication(sys.argv)
    app.setStyle('Windows')
    ex = MainWindow()

    dummy = subprocess.Popen(
        ["java", "-jar", "appatcher/thirdparty/apktool/apktool_2.5.0.jar", "h"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True)
    out, err = dummy.communicate()
    ex.outputTextBrowser.append(out)

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
