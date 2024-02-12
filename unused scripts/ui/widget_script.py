from PySide6.QtWidgets import QWidget
from ui.widget_old import Ui_arbitrage_info

# Created: Sunday, August 14, 2022, 10:09:41 AM


class WidgetScript(QWidget):

    def __init__(self, info: str, parent=None):
        # initializing our widget
        super(WidgetScript, self).__init__(parent)
        self.ui = Ui_arbitrage_info()
        self.ui.setupUi(self)
        # displaying arbitrage info
        self.ui.difference_field.setText(info.split(' ')[0])
        self.ui.for_buy_field.setText(info.split(' ')[1] + ' ' + info.split(' ')[2])
        self.ui.for_sell_field.setText(info.split(' ')[3] + ' ' + info.split(' ')[4])
        #self.ui.difference.setText(info.split(' ')[0])
        #self.ui.exchange_1.setText(info.split(' ')[1])
        #self.ui.pair_1.setText(info.split(' ')[2])
        #self.ui.exchange_2.setText(info.split(' ')[3])
        #self.ui.pair_2.setText(info.split(' ')[4])
