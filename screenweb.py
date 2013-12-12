#! /usr/bin/env python
import os
import sys
import time
from PyQt4.QtGui import QPixmap, QApplication

class ScreenWeb(QApplication):

    def __init__(self, window_id=None):
        super(ScreenWeb, self).__init__(sys.argv)
        if not window_id:
            window_id = QApplication.desktop().winId()
        else:
            window_id = int(window_id, 0)
        while True:
            QPixmap.grabWindow(window_id).save('new_image.png', 'png')
            os.rename('new_image.png', 'image.png')
            time.sleep(0.3)

def main():
    window_id = sys.argv[1] if len(sys.argv) > 1 else None
    ScreenWeb(window_id)

if __name__ == '__main__':
    main()
