#  Copyright (c) 2020. Mohamed Zumair <mhdzumair@gmail.com>

import sys
from PySide2.QtWidgets import QApplication
from control import Control


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Jilebi")
    # app.setStyle("Breeze")
    window = Control()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
