import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication
from ui.design import Ui_MainWindow
from all_exchanges_parser import AllExchangesParser
import asyncio
import qasync

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

# Created: Sunday, August 14, 2022, 10:09:41 AM


class MainWindowScript(QMainWindow):

    def __init__(self):
        super(MainWindowScript, self).__init__()
        self._initialize_window()
        self._set_actions_to_buttons()
        # for dragging
        self.ui.background_frame.mouseMoveEvent = self._move_window
        self._start_pose = None

    def _initialize_window(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def _set_actions_to_buttons(self):
        self.ui.minimize.clicked.connect(lambda: self.showMinimized())
        self.ui.exit.clicked.connect(lambda: self.close())
        self.ui.get_info.clicked.connect(self._get_money)

    def _move_window(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPosition().toPoint() - self._start_pose)
            self._start_pose = event.globalPosition().toPoint()
            event.accept()

    def mousePressEvent(self, event):
        self._start_pose = event.globalPosition().toPoint()

    @qasync.asyncSlot()
    async def _get_money(self):
        await AllExchangesParser().get_exchanges_pairs()
        #for item in PrepareForCompare().selection_for_compare(res):
            #widget = WidgetScript(info=item)
            #self.ui.for_all_info.addWidget(widget)


"""if __name__ == '__main__':
    app = QApplication()
    window = MainWindowScript()
    window.show()
    sys.exit(app.exec())"""


def main():
    app = QApplication(sys.argv)
    loop = qasync.QEventLoop(app)
    asyncio.set_event_loop(loop)
    w = MainWindowScript()
    w.show()
    loop.run_forever()


if __name__ == "__main__":
    main()
