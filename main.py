import sys
from PyQt5.QtWidgets import QApplication
from gui import VisionLingoApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VisionLingoApp()
    window.show()
    sys.exit(app.exec_())
