

################################################################################
## Form generated from reading UI file 'design.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1145, 570)
        MainWindow.setMinimumSize(QSize(1, 1))
        MainWindow.setMaximumSize(QSize(2000, 1000))
        icon = QIcon()
        icon.addFile(u":/icons/icons/diamond_final.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"QWidget{\n"
"color: rgb(237, 235, 237);\n"
"font: 21pt \"MS Serif\";\n"
"}\n"
"\n"
"QFrame {\n"
"background-color: rgb(174, 168, 251);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QPushButton{\n"
"	border: none;\n"
"	background-color:  rgb(150, 147, 235);\n"
"	/*border: 3px solid;*/\n"
"	border-radius: 10px;\n"
"	border-color: rgb(237, 235, 237);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:  rgb(124, 126, 208);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color:  rgb(174, 168, 251);\n"
"}\n"
"\n"
"\n"
"\n"
"                                                 /* ScrollBar */\n"
"\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color:  rgb(124, 126, 208);\n"
"	min-height: 30px;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	"
                        "background-color: transparent;\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"")
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        MainWindow.setIconSize(QSize(32, 32))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.centralwidget.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.main_window_layout = QVBoxLayout(self.centralwidget)
        self.main_window_layout.setSpacing(3)
        self.main_window_layout.setObjectName(u"main_window_layout")
        self.main_window_layout.setContentsMargins(10, 10, 10, 10)
        self.background_frame = QFrame(self.centralwidget)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setStyleSheet(u"")
        self.background_frame.setFrameShape(QFrame.NoFrame)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.my_logo = QLabel(self.background_frame)
        self.my_logo.setObjectName(u"my_logo")
        self.my_logo.setGeometry(QRect(-30, 140, 371, 221))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.my_logo.sizePolicy().hasHeightForWidth())
        self.my_logo.setSizePolicy(sizePolicy)
        self.my_logo.setStyleSheet(u"image: url(:/icons/pixel_logo.png);")
        self.cloud_1 = QLabel(self.background_frame)
        self.cloud_1.setObjectName(u"cloud_1")
        self.cloud_1.setGeometry(QRect(10, 490, 151, 101))
        self.cloud_1.setStyleSheet(u"image: url(:/icons/cloud_1.png);")
        self.cloud_1.setFrameShape(QFrame.NoFrame)
        self.cloud_3 = QLabel(self.background_frame)
        self.cloud_3.setObjectName(u"cloud_3")
        self.cloud_3.setGeometry(QRect(-20, -10, 121, 81))
        self.cloud_3.setStyleSheet(u"image: url(:/icons/cloud_1.png);")
        self.cloud_3.setFrameShape(QFrame.NoFrame)
        self.cloud_4 = QLabel(self.background_frame)
        self.cloud_4.setObjectName(u"cloud_4")
        self.cloud_4.setGeometry(QRect(250, 20, 151, 101))
        self.cloud_4.setStyleSheet(u"image: url(:/icons/cloud_1.png);")
        self.cloud_4.setFrameShape(QFrame.NoFrame)
        self.cloud_5 = QLabel(self.background_frame)
        self.cloud_5.setObjectName(u"cloud_5")
        self.cloud_5.setGeometry(QRect(220, 350, 151, 101))
        self.cloud_5.setStyleSheet(u"image: url(:/icons/cloud_2.png);")
        self.cloud_5.setFrameShape(QFrame.NoFrame)
        self.cloud_6 = QLabel(self.background_frame)
        self.cloud_6.setObjectName(u"cloud_6")
        self.cloud_6.setGeometry(QRect(890, 20, 131, 91))
        self.cloud_6.setStyleSheet(u"image: url(:/icons/cloud_1.png);")
        self.cloud_6.setFrameShape(QFrame.NoFrame)
        self.cloud_7 = QLabel(self.background_frame)
        self.cloud_7.setObjectName(u"cloud_7")
        self.cloud_7.setGeometry(QRect(400, 490, 151, 101))
        self.cloud_7.setStyleSheet(u"image: url(:/icons/cloud_1.png);")
        self.cloud_7.setFrameShape(QFrame.NoFrame)
        self.cloud_8 = QLabel(self.background_frame)
        self.cloud_8.setObjectName(u"cloud_8")
        self.cloud_8.setGeometry(QRect(1050, 170, 151, 101))
        self.cloud_8.setStyleSheet(u"image: url(:/icons/cloud_2.png);")
        self.cloud_8.setFrameShape(QFrame.NoFrame)
        self.cloud_9 = QLabel(self.background_frame)
        self.cloud_9.setObjectName(u"cloud_9")
        self.cloud_9.setGeometry(QRect(870, 490, 151, 101))
        self.cloud_9.setStyleSheet(u"image: url(:/icons/cloud_2.png);")
        self.cloud_9.setFrameShape(QFrame.NoFrame)
        self.info_table = QFrame(self.background_frame)
        self.info_table.setObjectName(u"info_table")
        self.info_table.setGeometry(QRect(330, 60, 781, 481))
        self.info_table.setStyleSheet(u"/*background-color: rgb(174, 168, 251);*/\n"
"background-color:  rgb(150, 147, 235);\n"
"/* border: 4px solid;*/\n"
"border-color: rgb(255, 255, 255);")
        self.info_table.setFrameShape(QFrame.StyledPanel)
        self.info_table.setFrameShadow(QFrame.Raised)
        self.scrollArea = QScrollArea(self.info_table)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(9, 59, 761, 411))
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 761, 411))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.for_all_info = QVBoxLayout()
        self.for_all_info.setObjectName(u"for_all_info")
        self.for_all_info.setSizeConstraint(QLayout.SetMinAndMaxSize)

        self.gridLayout.addLayout(self.for_all_info, 2, 0, 1, 2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_2 = QWidget(self.info_table)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(20, 10, 741, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_4 = QSpacerItem(120, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.label_2 = QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer_5 = QSpacerItem(120, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.label_3 = QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.label_3)

        self.horizontalSpacer_6 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)

        self.horizontalLayoutWidget = QWidget(self.background_frame)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(330, 10, 781, 41))
        self.top_panel = QHBoxLayout(self.horizontalLayoutWidget)
        self.top_panel.setObjectName(u"top_panel")
        self.top_panel.setContentsMargins(0, 0, 0, 0)
        self.get_info = QPushButton(self.horizontalLayoutWidget)
        self.get_info.setObjectName(u"get_info")
        self.get_info.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.get_info.sizePolicy().hasHeightForWidth())
        self.get_info.setSizePolicy(sizePolicy2)
        self.get_info.setLayoutDirection(Qt.LeftToRight)
        self.get_info.setStyleSheet(u"")

        self.top_panel.addWidget(self.get_info)

        self.horizontalSpacer_2 = QSpacerItem(90, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.top_panel.addItem(self.horizontalSpacer_2)

        self.telegram_nickname = QLabel(self.horizontalLayoutWidget)
        self.telegram_nickname.setObjectName(u"telegram_nickname")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.telegram_nickname.sizePolicy().hasHeightForWidth())
        self.telegram_nickname.setSizePolicy(sizePolicy3)
        self.telegram_nickname.setLayoutDirection(Qt.LeftToRight)
        self.telegram_nickname.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.top_panel.addWidget(self.telegram_nickname)

        self.horizontalSpacer = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.top_panel.addItem(self.horizontalSpacer)

        self.minimize = QPushButton(self.horizontalLayoutWidget)
        self.minimize.setObjectName(u"minimize")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.minimize.sizePolicy().hasHeightForWidth())
        self.minimize.setSizePolicy(sizePolicy4)
        self.minimize.setMinimumSize(QSize(40, 0))
        self.minimize.setStyleSheet(u"image: url(:/icons/minimize_button.png);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/minimize_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize.setIcon(icon1)
        self.minimize.setIconSize(QSize(20, 20))

        self.top_panel.addWidget(self.minimize)

        self.exit = QPushButton(self.horizontalLayoutWidget)
        self.exit.setObjectName(u"exit")
        sizePolicy4.setHeightForWidth(self.exit.sizePolicy().hasHeightForWidth())
        self.exit.setSizePolicy(sizePolicy4)
        self.exit.setMinimumSize(QSize(40, 0))
        self.exit.setStyleSheet(u"image: url(:/icons/close_button.png);")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/close_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exit.setIcon(icon2)
        self.exit.setIconSize(QSize(20, 20))

        self.top_panel.addWidget(self.exit)


        self.main_window_layout.addWidget(self.background_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"my_soul", None))
        self.my_logo.setText("")
        self.cloud_1.setText("")
        self.cloud_3.setText("")
        self.cloud_4.setText("")
        self.cloud_5.setText("")
        self.cloud_6.setText("")
        self.cloud_7.setText("")
        self.cloud_8.setText("")
        self.cloud_9.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"difference", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"for buy info", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"for sell info", None))
        self.get_info.setText(QCoreApplication.translate("MainWindow", u"get info", None))
        self.telegram_nickname.setText(QCoreApplication.translate("MainWindow", u"my telegram: @pleasant_user", None))
        self.minimize.setText("")
        self.exit.setText("")
    # retranslateUi

