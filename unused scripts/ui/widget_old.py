

################################################################################
## Form generated from reading UI file 'widget_old.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QSizePolicy, QWidget)

class Ui_arbitrage_info(object):
    def setupUi(self, arbitrage_info):
        if not arbitrage_info.objectName():
            arbitrage_info.setObjectName(u"arbitrage_info")
        arbitrage_info.resize(530, 52)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(arbitrage_info.sizePolicy().hasHeightForWidth())
        arbitrage_info.setSizePolicy(sizePolicy)
        arbitrage_info.setStyleSheet(u"QWidget{\n"
"background-color:  rgb(150, 147, 235);\n"
"color: rgb(237, 235, 237);\n"
"font: 18pt \"MS Serif\";\n"
"}")
        arbitrage_info.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.horizontalLayout = QHBoxLayout(arbitrage_info)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(arbitrage_info)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"border: none;")
        self.difference_field = QLabel(self.groupBox)
        self.difference_field.setObjectName(u"difference_field")
        self.difference_field.setGeometry(QRect(20, -9, 80, 51))
        self.for_buy_field = QLabel(self.groupBox)
        self.for_buy_field.setObjectName(u"for_buy_field")
        self.for_buy_field.setGeometry(QRect(170, -9, 80, 51))
        self.for_sell_field = QLabel(self.groupBox)
        self.for_sell_field.setObjectName(u"for_sell_field")
        self.for_sell_field.setGeometry(QRect(340, -10, 80, 51))

        self.horizontalLayout.addWidget(self.groupBox)


        self.retranslateUi(arbitrage_info)

        QMetaObject.connectSlotsByName(arbitrage_info)
    # setupUi

    def retranslateUi(self, arbitrage_info):
        arbitrage_info.setWindowTitle(QCoreApplication.translate("arbitrage_info", u"Form", None))
        self.groupBox.setTitle("")
        self.difference_field.setText(QCoreApplication.translate("arbitrage_info", u"TextLabel", None))
        self.for_buy_field.setText(QCoreApplication.translate("arbitrage_info", u"TextLabel", None))
        self.for_sell_field.setText(QCoreApplication.translate("arbitrage_info", u"TextLabel", None))
    # retranslateUi

