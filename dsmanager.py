# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'account_reporter.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QMetaObject,
    QRect,
    QSize,
    QTime,
    Qt,
)
from PySide2.QtGui import (
    QBrush,
    QColor,
    QFont,
    QIcon,
    QLinearGradient,
    QPalette,
    QPixmap,
    QGradient,
)
from PySide2.QtWidgets import *

import includes_rc


class Ui_DedSecWindow(object):
    def setupUi(self, DedSecWindow):
        if not DedSecWindow.objectName():
            DedSecWindow.setObjectName(u"DedSecWindow")
        DedSecWindow.setWindowModality(Qt.WindowModal)
        DedSecWindow.resize(1011, 934)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DedSecWindow.sizePolicy().hasHeightForWidth())
        DedSecWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Arial Narrow")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        DedSecWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"inc/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        DedSecWindow.setWindowIcon(icon)
        DedSecWindow.setStyleSheet(
            u"QMainWindow{\n"
            "background-image:url(:/images/background.jpg);\n"
            "background-repeat:none;\n"
            "}\n"
            "QPushButton {\n"
            "	border: 2px solid rgb(52, 59, 72);\n"
            "	border-radius: 5px;	\n"
            "	background-color: rgb(199, 200, 255);\n"
            "	padding: 5px\n"
            "}\n"
            "QPushButton:hover {\n"
            "	border: 2px solid rgb(61, 70, 86);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	background-color: rgb(35, 40, 49);\n"
            "	border: 2px solid rgb(43, 50, 61);\n"
            "}"
        )
        DedSecWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        DedSecWindow.setAnimated(True)
        DedSecWindow.setDocumentMode(False)
        DedSecWindow.setDockNestingEnabled(True)
        self.actionAbut_DS_Manager = QAction(DedSecWindow)
        self.actionAbut_DS_Manager.setObjectName(u"actionAbut_DS_Manager")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbut_DS_Manager.setIcon(icon1)
        self.actionAbut_DS_Manager.setShortcutContext(Qt.WidgetShortcut)
        self.actionAbut_DS_Manager.setMenuRole(QAction.TextHeuristicRole)
        self.actionBackup_Database = QAction(DedSecWindow)
        self.actionBackup_Database.setObjectName(u"actionBackup_Database")
        self.centralwidget = QWidget(DedSecWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(
            250, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(10)
        sizePolicy1.setVerticalStretch(10)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMaximumSize(QSize(250, 250))
        self.label.setStyleSheet(
            u"QLabel{\n"
            "	border-radius: 25px;\n"
            "	padding: 20px;\n"
            "	width: 200px;\n"
            "	height: 150px; \n"
            "}"
        )
        self.label.setPixmap(QPixmap(u":/images/mosque.jpg"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(
            150, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setFamily(u"Tahoma")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.label_11.setFont(font1)
        self.label_11.setLayoutDirection(Qt.RightToLeft)
        self.label_11.setStyleSheet(
            u"color: white;\n" "padding:10px;\n" "text-align:left;"
        )
        self.label_11.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.label_11.setWordWrap(False)
        self.label_11.setMargin(10)
        self.label_11.setOpenExternalLinks(False)

        self.horizontalLayout.addWidget(self.label_11)

        self.horizontalSpacer_2 = QSpacerItem(
            250, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(60, 10, 30, 25)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMaximumSize(QSize(1500, 16777215))
        font2 = QFont()
        font2.setFamily(u"Tahoma")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setWeight(75)
        self.tabWidget.setFont(font2)
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setToolTipDuration(-1)
        # if QT_CONFIG(accessibility)
        self.tabWidget.setAccessibleDescription(u"")
        # endif // QT_CONFIG(accessibility)
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(
            u"QWidget{\n"
            "	background-color:qlineargradient(spread:pad, x1:0.532552, y1:0, x2:0.522, y2:0.926136, stop:0.0199005 rgba(173, 224, 209, 207), stop:0.965174 rgba(165, 218, 214, 170));\n"
            "	border:0px;\n"
            "	height:30%;\n"
            "}\n"
            "\n"
            "QTabWidget::pane {\n"
            "	border: 0;\n"
            "	background-color:rgb(220, 255, 247);\n"
            "	border-radius: 10px;\n"
            "}\n"
            "\n"
            "QCalendarWidget QToolButton{\n"
            "  	color: black;\n"
            "  	background-color:rgb(156, 255, 231);\n"
            "}\n"
            "\n"
            " \n"
            "\n"
            "QCalendarWidget QAbstractItemView:enabled \n"
            "  {\n"
            "  \n"
            "  	color: black;  \n"
            "  	background-color: rgb(198, 255, 232);  \n"
            "  	selection-background-color: rgb(64, 64, 64); \n"
            "  	selection-color: rgb(0, 255, 0); \n"
            "  }\n"
            "\n"
            "QTabBar::tab {\n"
            "	width: 200;\n"
            "	background: gray;\n"
            "	color: white;\n"
            "	padding: 10px; \n"
            "	border-radius: 40px;\n"
            "}\n"
            "\n"
            "QTabBar::tab:selected {\n"
            "	background: qlineargradient(spread:pad, x1:0.532552, y1:0, x2:0.522, y2:0.926136, stop:0.0199005 rgba(173, 224, 209, 207), stop:0.965174 rgba(165, 218,"
            " 214, 170));\n"
            "	color: rgb(9, 0, 79);\n"
            "	padding: 10px; \n"
            "	border-radius: 40px;\n"
            "}"
        )
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setIconSize(QSize(0, 0))
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.data_entry_tab = QWidget()
        self.data_entry_tab.setObjectName(u"data_entry_tab")
        font3 = QFont()
        font3.setBold(False)
        font3.setWeight(50)
        self.data_entry_tab.setFont(font3)
        self.gridLayout = QGridLayout(self.data_entry_tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(30)
        self.gridLayout.setContentsMargins(80, 40, 20, 10)
        self.label_10 = QLabel(self.data_entry_tab)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)
        font4 = QFont()
        font4.setFamily(u"Candara")
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setItalic(False)
        font4.setWeight(75)
        font4.setStrikeOut(False)
        font4.setStyleStrategy(QFont.PreferAntialias)
        self.label_10.setFont(font4)
        self.label_10.setStyleSheet(u"")

        self.gridLayout.addWidget(self.label_10, 5, 1, 1, 1)

        self.trans_type = QComboBox(self.data_entry_tab)
        self.trans_type.addItem(u"Income")
        self.trans_type.addItem("")
        self.trans_type.addItem("")
        self.trans_type.addItem("")
        self.trans_type.setObjectName(u"trans_type")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.trans_type.sizePolicy().hasHeightForWidth())
        self.trans_type.setSizePolicy(sizePolicy3)
        self.trans_type.setMaximumSize(QSize(300, 16777215))
        font5 = QFont()
        font5.setFamily(u"Candara")
        font5.setPointSize(11)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setWeight(75)
        self.trans_type.setFont(font5)
        self.trans_type.setStyleSheet(
            u"QComboBox{\n"
            "	 background-color:qlineargradient(spread:pad, x1:0.532552, y1:0, x2:0.522, y2:0.926136, stop:0.0199005 rgba(50, 186, 144, 52), stop:0.482587 rgba(65, 156, 128, 54), stop:0.975124 rgba(75, 164, 181, 80));\n"
            "	\n"
            "		\n"
            "	\n"
            "\n"
            "	\n"
            "\n"
            "    \n"
            "}\n"
            "QComboBox:hover{\n"
            "	border: 2px solid rgb(64, 71, 88);\n"
            "   \n"
            "	\n"
            "}\n"
            "QComboBox QAbstractItemView {\n"
            "	padding: 10px;\n"
            "\n"
            "	background-color:rgb(170, 255, 230)\n"
            "	\n"
            " \n"
            "}\n"
            "\n"
            "QComboBox QAbstractItemView{border-radius: 5px;\n"
            "	border: 2px ;\n"
            "	padding: 5px;\n"
            "	padding-left: 10px;\n"
            "    }"
        )
        self.trans_type.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.trans_type.setFrame(True)

        self.gridLayout.addWidget(self.trans_type, 1, 7, 1, 1)

        self.label_5 = QLabel(self.data_entry_tab)
        self.label_5.setObjectName(u"label_5")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy4)
        self.label_5.setFont(font4)

        self.gridLayout.addWidget(self.label_5, 6, 1, 1, 1)

        self.money = QLineEdit(self.data_entry_tab)
        self.money.setObjectName(u"money")
        sizePolicy3.setHeightForWidth(self.money.sizePolicy().hasHeightForWidth())
        self.money.setSizePolicy(sizePolicy3)
        self.money.setMaximumSize(QSize(200, 16777215))
        font6 = QFont()
        font6.setFamily(u"Candara")
        font6.setPointSize(12)
        font6.setBold(True)
        font6.setItalic(False)
        font6.setWeight(75)
        self.money.setFont(font6)
        self.money.setStyleSheet(
            u"QLineEdit {\n"
            "	border-radius: 5px;\n"
            "	border: 2px solid rgb(27, 29, 35);\n"
            "	padding-left: 10px;\n"
            "}\n"
            "QLineEdit:hover {\n"
            "	border: 2px solid rgb(64, 71, 88);\n"
            "}\n"
            "QLineEdit:focus {\n"
            "	border: 2px solid rgb(91, 101, 124);\n"
            "}"
        )
        self.money.setInputMethodHints(Qt.ImhDigitsOnly)
        self.money.setText(u"")
        self.money.setFrame(True)
        self.money.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.money, 6, 7, 1, 1)

        self.label_4 = QLabel(self.data_entry_tab)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"")

        self.gridLayout.addWidget(self.label_4, 4, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radioButton_2 = QRadioButton(self.data_entry_tab)
        self.radioButton_2.setObjectName(u"radioButton_2")
        font7 = QFont()
        font7.setFamily(u"Candara")
        font7.setPointSize(10)
        font7.setBold(True)
        font7.setItalic(False)
        font7.setWeight(75)
        self.radioButton_2.setFont(font7)

        self.horizontalLayout_2.addWidget(self.radioButton_2)

        self.radioButton = QRadioButton(self.data_entry_tab)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setFont(font7)

        self.horizontalLayout_2.addWidget(self.radioButton)

        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 7, 1, 1)

        self.clear_entry_button = QPushButton(self.data_entry_tab)
        self.clear_entry_button.setObjectName(u"clear_entry_button")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(
            self.clear_entry_button.sizePolicy().hasHeightForWidth()
        )
        self.clear_entry_button.setSizePolicy(sizePolicy5)
        font8 = QFont()
        font8.setFamily(u"Tahoma")
        font8.setPointSize(9)
        font8.setBold(True)
        font8.setItalic(False)
        font8.setWeight(75)
        self.clear_entry_button.setFont(font8)
        self.clear_entry_button.setStyleSheet(
            u"QPushButton{\n"
            "background-color:qlineargradient(spread:pad, x1:0.532552, y1:0, x2:0.522, y2:0.926136, stop:0.0547264 rgba(10, 103, 95, 209), stop:1 rgba(13, 136, 125, 209));\n"
            "width:110%;\n"
            "height:40%;\n"
            "color:white;\n"
            "border-radius:8px;\n"
            "}\n"
            "\n"
            "\n"
            "  QPushButton:hover:!pressed\n"
            "{\n"
            "  border: 2px solid rgb(41, 135, 140);\n"
            "background-color:rgb(199, 248, 255);\n"
            "color:black;\n"
            "\n"
            "}"
        )
        self.clear_entry_button.setIconSize(QSize(40, 40))

        self.gridLayout.addWidget(self.clear_entry_button, 11, 2, 1, 1)

        self.label_2 = QLabel(self.data_entry_tab)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setFont(font4)

        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        self.label_9 = QLabel(self.data_entry_tab)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setFont(font4)

        self.gridLayout.addWidget(self.label_9, 3, 1, 1, 4)

        self.enter_data_button = QPushButton(self.data_entry_tab)
        self.enter_data_button.setObjectName(u"enter_data_button")
        sizePolicy5.setHeightForWidth(
            self.enter_data_button.sizePolicy().hasHeightForWidth()
        )
        self.enter_data_button.setSizePolicy(sizePolicy5)
        self.enter_data_button.setFont(font8)
        self.enter_data_button.setStyleSheet(
            u"QPushButton{\n"
            "background-color:qlineargradient(spread:pad, x1:0.532552, y1:0, x2:0.522, y2:0.926136, stop:0.0547264 rgba(10, 103, 95, 209), stop:1 rgba(13, 136, 125, 209));\n"
            "width:110%;\n"
            "height:40%;\n"
            "color:white;\n"
            "border-radius:8px;\n"
            "}\n"
            "\n"
            "\n"
            "  QPushButton:hover:!pressed\n"
            "{\n"
            "  border: 2px solid rgb(41, 135, 140);\n"
            "background-color:rgb(199, 248, 255);\n"
            "color:black;\n"
            "\n"
            "}"
        )

        self.gridLayout.addWidget(self.enter_data_button, 11, 4, 1, 1)

        self.date_of_entry = QDateEdit(self.data_entry_tab)
        self.date_of_entry.setObjectName(u"date_of_entry")
        sizePolicy3.setHeightForWidth(
            self.date_of_entry.sizePolicy().hasHeightForWidth()
        )
        self.date_of_entry.setSizePolicy(sizePolicy3)
        self.date_of_entry.setMaximumSize(QSize(130, 16777215))
        self.date_of_entry.setFont(font5)
        self.date_of_entry.setStyleSheet(
            u"QDateEdit{\n"
            "	border-radius: 5px;\n"
            "	border: 2px solid rgb(27, 29, 35);\n"
            "	padding: 5px;\n"
            "	padding-left: 10px;\n"
            "\n"
            "   background-color:qlineargradient(spread:pad, x1:0.532552, y1:0, x2:0.522, y2:0.926136, stop:0.0199005 rgba(50, 186, 144, 52), stop:0.482587 rgba(65, 156, 128, 54), stop:0.975124 rgba(75, 164, 181, 80));\n"
            "		\n"
            "		\n"
            "}\n"
            "QDateEdit:hover{\n"
            "	border: 2px solid rgb(64, 71, 88);\n"
            "   \n"
            "	\n"
            "		\n"
            "  \n"
            "}\n"
            "\n"
            "QCalendarWidget QToolButton{\n"
            "\n"
            "  	color: black;\n"
            "  	background-color:rgb(156, 255, 231);}\n"
            "\n"
            " \n"
            "\n"
            "QCalendarWidget QAbstractItemView:enabled \n"
            "  {\n"
            "  \n"
            "  	color: black;  \n"
            "  	background-color: rgb(198, 255, 232);  \n"
            "  	selection-background-color: rgb(64, 64, 64); \n"
            "  	selection-color: rgb(0, 255, 0); \n"
            "  }"
        )
        self.date_of_entry.setMinimumDateTime(
            QDateTime(QDate(1767, 9, 14), QTime(0, 0, 0))
        )
        self.date_of_entry.setCalendarPopup(True)

        self.gridLayout.addWidget(self.date_of_entry, 4, 7, 1, 1)

        self.label_3 = QLabel(self.data_entry_tab)
        self.label_3.setObjectName(u"label_3")
        sizePolicy4.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy4)
        self.label_3.setFont(font4)

        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(
            100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout.addItem(self.horizontalSpacer_8, 11, 7, 1, 1)

        self.more_trans_detail = QLineEdit(self.data_entry_tab)
        self.more_trans_detail.setObjectName(u"more_trans_detail")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(
            self.more_trans_detail.sizePolicy().hasHeightForWidth()
        )
        self.more_trans_detail.setSizePolicy(sizePolicy6)
        self.more_trans_detail.setMaximumSize(QSize(300, 16777215))
        self.more_trans_detail.setFont(font6)
        self.more_trans_detail.setStyleSheet(
            u"QLineEdit {\n"
            "	border-radius: 5px;\n"
            "	border: 2px solid rgb(27, 29, 35);\n"
            "	padding-left: 10px;\n"
            "}\n"
            "QLineEdit:hover {\n"
            "	border: 2px solid rgb(64, 71, 88);\n"
            "}\n"
            "QLineEdit:focus {\n"
            "	border: 2px solid rgb(91, 101, 124);\n"
            "}"
        )
        self.more_trans_detail.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.more_trans_detail.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.more_trans_detail, 3, 7, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(
            100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout.addItem(self.horizontalSpacer_9, 11, 3, 1, 1)

        self.method_of_trans = QComboBox(self.data_entry_tab)
        self.method_of_trans.setObjectName(u"method_of_trans")
        sizePolicy3.setHeightForWidth(
            self.method_of_trans.sizePolicy().hasHeightForWidth()
        )
        self.method_of_trans.setSizePolicy(sizePolicy3)
        self.method_of_trans.setMaximumSize(QSize(300, 16777215))
        palette = QPalette()
        gradient = QLinearGradient(0.532552, 0, 0.522, 0.926136)
        gradient.setSpread(QGradient.PadSpread)
        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0199005, QColor(50, 186, 144, 52))
        gradient.setColorAt(0.482587, QColor(65, 156, 128, 54))
        gradient.setColorAt(0.975124, QColor(75, 164, 181, 80))
        brush = QBrush(gradient)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        gradient1 = QLinearGradient(0.532552, 0, 0.522, 0.926136)
        gradient1.setSpread(QGradient.PadSpread)
        gradient1.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient1.setColorAt(0.0199005, QColor(50, 186, 144, 52))
        gradient1.setColorAt(0.482587, QColor(65, 156, 128, 54))
        gradient1.setColorAt(0.975124, QColor(75, 164, 181, 80))
        brush1 = QBrush(gradient1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        gradient2 = QLinearGradient(0.532552, 0, 0.522, 0.926136)
        gradient2.setSpread(QGradient.PadSpread)
        gradient2.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient2.setColorAt(0.0199005, QColor(50, 186, 144, 52))
        gradient2.setColorAt(0.482587, QColor(65, 156, 128, 54))
        gradient2.setColorAt(0.975124, QColor(75, 164, 181, 80))
        brush2 = QBrush(gradient2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush2)
        gradient3 = QLinearGradient(0.532552, 0, 0.522, 0.926136)
        gradient3.setSpread(QGradient.PadSpread)
        gradient3.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient3.setColorAt(0.0199005, QColor(50, 186, 144, 52))
        gradient3.setColorAt(0.482587, QColor(65, 156, 128, 54))
        gradient3.setColorAt(0.975124, QColor(75, 164, 181, 80))
        brush3 = QBrush(gradient3)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        gradient4 = QLinearGradient(0.532552, 0, 0.522, 0.926136)
        gradient4.setSpread(QGradient.PadSpread)
        gradient4.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient4.setColorAt(0.0199005, QColor(50, 186, 144, 52))
        gradient4.setColorAt(0.482587, QColor(65, 156, 128, 54))
        gradient4.setColorAt(0.975124, QColor(75, 164, 181, 80))
        brush4 = QBrush(gradient4)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        gradient5 = QLinearGradient(0.532552, 0, 0.522, 0.926136)
        gradient5.setSpread(QGradient.PadSpread)
        gradient5.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient5.setColorAt(0.0199005, QColor(50, 186, 144, 52))
        gradient5.setColorAt(0.482587, QColor(65, 156, 128, 54))
        gradient5.setColorAt(0.975124, QColor(75, 164, 181, 80))
        brush5 = QBrush(gradient5)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        gradient6 = QLinearGradient(0.532552, 0, 0.522, 0.926136)
        gradient6.setSpread(QGradient.PadSpread)
        gradient6.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient6.setColorAt(0.0199005, QColor(50, 186, 144, 52))
        gradient6.setColorAt(0.482587, QColor(65, 156, 128, 54))
        gradient6.setColorAt(0.975124, QColor(75, 164, 181, 80))
        brush6 = QBrush(gradient6)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        gradient7 = QLinearGradient(0.532552, 0, 0.522, 0.926136)
        gradient7.setSpread(QGradient.PadSpread)
        gradient7.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient7.setColorAt(0.0199005, QColor(50, 186, 144, 52))
        gradient7.setColorAt(0.482587, QColor(65, 156, 128, 54))
        gradient7.setColorAt(0.975124, QColor(75, 164, 181, 80))
        brush7 = QBrush(gradient7)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        gradient8 = QLinearGradient(0.532552, 0, 0.522, 0.926136)
        gradient8.setSpread(QGradient.PadSpread)
        gradient8.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient8.setColorAt(0.0199005, QColor(50, 186, 144, 52))
        gradient8.setColorAt(0.482587, QColor(65, 156, 128, 54))
        gradient8.setColorAt(0.975124, QColor(75, 164, 181, 80))
        brush8 = QBrush(gradient8)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        self.method_of_trans.setPalette(palette)
        self.method_of_trans.setFont(font6)
        self.method_of_trans.setStyleSheet(
            u"QComboBox{\n"
            "	 background-color:qlineargradient(spread:pad, x1:0.532552, y1:0, x2:0.522, y2:0.926136, stop:0.0199005 rgba(50, 186, 144, 52), stop:0.482587 rgba(65, 156, 128, 54), stop:0.975124 rgba(75, 164, 181, 80));\n"
            "}\n"
            "QComboBox:hover{\n"
            "	border: 2px solid rgb(64, 71, 88);\n"
            "   \n"
            "}\n"
            "QComboBox QAbstractItemView {\n"
            "	padding: 10px;\n"
            "\n"
            "	background-color:rgb(170, 255, 230)\n"
            "	\n"
            " \n"
            "}\n"
            "\n"
            "QComboBox QAbstractItemView{border-radius: 5px;\n"
            "	border: 2px ;\n"
            "	padding: 5px;\n"
            "	padding-left: 10px;\n"
            "    }"
        )

        self.gridLayout.addWidget(self.method_of_trans, 2, 7, 1, 1)

        self.tabWidget.addTab(self.data_entry_tab, "")
        self.report_gen_tab = QWidget()
        self.report_gen_tab.setObjectName(u"report_gen_tab")
        self.gridLayout_2 = QGridLayout(self.report_gen_tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setVerticalSpacing(20)
        self.gridLayout_2.setContentsMargins(80, 20, 20, 10)
        self.label_6 = QLabel(self.report_gen_tab)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        self.label_6.setFont(font8)

        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)

        self.report_date_from = QDateEdit(self.report_gen_tab)
        self.report_date_from.setObjectName(u"report_date_from")
        sizePolicy5.setHeightForWidth(
            self.report_date_from.sizePolicy().hasHeightForWidth()
        )
        self.report_date_from.setSizePolicy(sizePolicy5)
        font9 = QFont()
        font9.setFamily(u"Candara")
        font9.setPointSize(11)
        font9.setBold(True)
        font9.setItalic(False)
        font9.setUnderline(False)
        font9.setWeight(75)
        self.report_date_from.setFont(font9)
        self.report_date_from.setStyleSheet(
            u"QDateEdit{\n"
            "	border-radius: 5px;\n"
            "	border: 2px solid rgb(27, 29, 35);\n"
            "	padding: 5px;\n"
            "	padding-left: 10px;\n"
            "\n"
            "   background-color:qlineargradient(spread:pad, x1:0.532552, y1:0, x2:0.522, y2:0.926136, stop:0.0199005 rgba(50, 186, 144, 52), stop:0.482587 rgba(65, 156, 128, 54), stop:0.975124 rgba(75, 164, 181, 80));\n"
            "		\n"
            "		\n"
            "}\n"
            "QDateEdit:hover{\n"
            "	border: 2px solid rgb(64, 71, 88);\n"
            "   \n"
            "	\n"
            "		\n"
            "  \n"
            "}\n"
            "\n"
            "QCalendarWidget QToolButton{\n"
            "\n"
            "  	color: black;\n"
            "  	background-color:rgb(156, 255, 231);}\n"
            "\n"
            " \n"
            "\n"
            "QCalendarWidget QAbstractItemView:enabled \n"
            "  {\n"
            "  \n"
            "  	color: black;  \n"
            "  	background-color: rgb(198, 255, 232);  \n"
            "  	selection-background-color: rgb(64, 64, 64); \n"
            "  	selection-color: rgb(0, 255, 0); \n"
            "  }"
        )
        self.report_date_from.setDateTime(QDateTime(QDate(2020, 1, 1), QTime(0, 0, 0)))
        self.report_date_from.setMinimumDateTime(
            QDateTime(QDate(2010, 9, 14), QTime(0, 0, 0))
        )
        self.report_date_from.setMaximumDate(QDate(9999, 11, 30))
        self.report_date_from.setCalendarPopup(True)
        self.report_date_from.setDate(QDate(2020, 1, 1))

        self.gridLayout_2.addWidget(self.report_date_from, 3, 4, 1, 1)

        self.label_7 = QLabel(self.report_gen_tab)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setFont(font8)

        self.gridLayout_2.addWidget(self.label_7, 4, 0, 1, 1)

        self.report_date_to = QDateEdit(self.report_gen_tab)
        self.report_date_to.setObjectName(u"report_date_to")
        sizePolicy5.setHeightForWidth(
            self.report_date_to.sizePolicy().hasHeightForWidth()
        )
        self.report_date_to.setSizePolicy(sizePolicy5)
        self.report_date_to.setFont(font9)
        self.report_date_to.setStyleSheet(
            u"QDateEdit{\n"
            "	border-radius: 5px;\n"
            "	border: 2px solid rgb(27, 29, 35);\n"
            "	padding: 5px;\n"
            "	padding-left: 10px;\n"
            "\n"
            "   background-color:qlineargradient(spread:pad, x1:0.532552, y1:0, x2:0.522, y2:0.926136, stop:0.0199005 rgba(50, 186, 144, 52), stop:0.482587 rgba(65, 156, 128, 54), stop:0.975124 rgba(75, 164, 181, 80));\n"
            "		\n"
            "		\n"
            "}\n"
            "QDateEdit:hover{\n"
            "	border: 2px solid rgb(64, 71, 88);\n"
            "   \n"
            "	\n"
            "		\n"
            "  \n"
            "}\n"
            "\n"
            "QCalendarWidget QToolButton{\n"
            "\n"
            "  	color: black;\n"
            "  	background-color:rgb(156, 255, 231);}\n"
            "\n"
            " \n"
            "\n"
            "QCalendarWidget QAbstractItemView:enabled \n"
            "  {\n"
            "  \n"
            "  	color: black;  \n"
            "  	background-color: rgb(198, 255, 232);  \n"
            "  	selection-background-color: rgb(64, 64, 64); \n"
            "  	selection-color: rgb(0, 255, 0); \n"
            "  }"
        )
        self.report_date_to.setWrapping(False)
        self.report_date_to.setReadOnly(False)
        self.report_date_to.setProperty("showGroupSeparator", False)
        self.report_date_to.setDateTime(QDateTime(QDate(2020, 1, 1), QTime(0, 0, 0)))
        self.report_date_to.setMinimumDateTime(
            QDateTime(QDate(2010, 9, 14), QTime(0, 0, 0))
        )
        self.report_date_to.setCurrentSection(QDateTimeEdit.DaySection)
        self.report_date_to.setCalendarPopup(True)
        self.report_date_to.setTimeSpec(Qt.TimeZone)

        self.gridLayout_2.addWidget(self.report_date_to, 4, 4, 1, 1)

        self.label_12 = QLabel(self.report_gen_tab)
        self.label_12.setObjectName(u"label_12")
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)
        font10 = QFont()
        font10.setFamily(u"Tahoma")
        font10.setPointSize(9)
        font10.setBold(True)
        font10.setWeight(75)
        self.label_12.setFont(font10)

        self.gridLayout_2.addWidget(self.label_12, 6, 0, 1, 1)

        self.comboBox = QComboBox(self.report_gen_tab)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy5.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy5)
        self.comboBox.setFont(font10)
        self.comboBox.setStyleSheet(
            u"QComboBox{\n"
            "	border-radius: 5px;\n"
            "	border: 2px solid rgb(27, 29, 35);\n"
            "	padding: 5px;\n"
            "	padding-left: 10px;\n"
            "}\n"
            "QComboBox:hover{\n"
            "	border: 2px solid rgb(64, 71, 88);\n"
            "}\n"
            "QComboBox QAbstractItemView {\n"
            "	padding: 10px;\n"
            "}"
        )

        self.gridLayout_2.addWidget(self.comboBox, 6, 4, 1, 1)

        self.print_report_button = QPushButton(self.report_gen_tab)
        self.print_report_button.setObjectName(u"print_report_button")
        sizePolicy5.setHeightForWidth(
            self.print_report_button.sizePolicy().hasHeightForWidth()
        )
        self.print_report_button.setSizePolicy(sizePolicy5)
        self.print_report_button.setFont(font5)
        self.print_report_button.setStyleSheet(
            u"QPushButton{\n"
            "background-color:qlineargradient(spread:pad, x1:0.532552, y1:0, x2:0.522, y2:0.926136, stop:0.0547264 rgba(10, 103, 95, 209), stop:1 rgba(13, 136, 125, 209));\n"
            "width:100%;\n"
            "height:40%;\n"
            "color:white;\n"
            "border-radius:8px;\n"
            "}\n"
            "\n"
            "QPushButton:hover:!pressed\n"
            "{\n"
            "  border: 2px solid rgb(41, 135, 140);\n"
            "background-color:rgb(199, 248, 255);\n"
            "color:black;\n"
            "}"
        )

        self.gridLayout_2.addWidget(self.print_report_button, 7, 1, 1, 1)

        self.preview_report_button = QPushButton(self.report_gen_tab)
        self.preview_report_button.setObjectName(u"preview_report_button")
        sizePolicy5.setHeightForWidth(
            self.preview_report_button.sizePolicy().hasHeightForWidth()
        )
        self.preview_report_button.setSizePolicy(sizePolicy5)
        self.preview_report_button.setFont(font5)
        self.preview_report_button.setStyleSheet(
            u"QPushButton{\n"
            "background-color:qlineargradient(spread:pad, x1:0.532552, y1:0, x2:0.522, y2:0.926136, stop:0.0547264 rgba(10, 103, 95, 209), stop:1 rgba(13, 136, 125, 209));\n"
            "width:130%;\n"
            "height:40%;\n"
            "color:white;\n"
            "border-radius:8px;\n"
            "}\n"
            "\n"
            "QPushButton:hover:!pressed\n"
            "{\n"
            "  border: 2px solid rgb(41, 135, 140);\n"
            "background-color:rgb(199, 248, 255);\n"
            "color:black;\n"
            "}"
        )

        self.gridLayout_2.addWidget(self.preview_report_button, 7, 2, 1, 1)

        self.export_pdf_button = QPushButton(self.report_gen_tab)
        self.export_pdf_button.setObjectName(u"export_pdf_button")
        sizePolicy5.setHeightForWidth(
            self.export_pdf_button.sizePolicy().hasHeightForWidth()
        )
        self.export_pdf_button.setSizePolicy(sizePolicy5)
        self.export_pdf_button.setFont(font5)
        self.export_pdf_button.setLayoutDirection(Qt.LeftToRight)
        self.export_pdf_button.setStyleSheet(
            u"QPushButton{\n"
            "background-color:qlineargradient(spread:pad, x1:0.532552, y1:0, x2:0.522, y2:0.926136, stop:0.0547264 rgba(10, 103, 95, 209), stop:1 rgba(13, 136, 125, 209));\n"
            "width:170%;\n"
            "height:40%;\n"
            "color:white;\n"
            "border-radius:8px;\n"
            "}\n"
            "\n"
            "QPushButton:hover:!pressed\n"
            "{\n"
            "  border: 2px solid rgb(41, 135, 140);\n"
            "background-color:rgb(199, 248, 255);\n"
            "color:black;\n"
            "}"
        )
        self.export_pdf_button.setFlat(False)

        self.gridLayout_2.addWidget(self.export_pdf_button, 7, 3, 1, 1)

        self.label_8 = QLabel(self.report_gen_tab)
        self.label_8.setObjectName(u"label_8")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy7)
        font11 = QFont()
        font11.setFamily(u"Tahoma")
        font11.setPointSize(15)
        font11.setBold(True)
        font11.setItalic(False)
        font11.setWeight(75)
        self.label_8.setFont(font11)
        self.label_8.setStyleSheet(
            u"background-color:rgba(0,0,0,0%);\n" "color:rgb(35, 93, 74)"
        )
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setMargin(10)

        self.gridLayout_2.addWidget(self.label_8, 0, 1, 1, 3)

        self.tabWidget.addTab(self.report_gen_tab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        DedSecWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(DedSecWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1011, 24))
        font12 = QFont()
        font12.setFamily(u"Candara")
        font12.setBold(True)
        font12.setWeight(75)
        self.menubar.setFont(font12)
        self.menubar.setStyleSheet(
            u"QMenuBar{\n"
            "background-color:rgb(122, 224, 210);\n"
            "}\n"
            "\n"
            "QMenu:!pressed\n"
            "{\n"
            "	selection-color: rgb(85, 0, 127);\n"
            "	background-color:rgb(139, 234, 255);\n"
            "}"
        )
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        DedSecWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(DedSecWindow)
        self.statusbar.setObjectName(u"statusbar")
        DedSecWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuAbout.addAction(self.actionAbut_DS_Manager)
        self.menuFile.addAction(self.actionBackup_Database)

        self.retranslateUi(DedSecWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(DedSecWindow)

    # setupUi

    def retranslateUi(self, DedSecWindow):
        DedSecWindow.setWindowTitle(
            QCoreApplication.translate("DedSecWindow", u"DS Manager", None)
        )
        self.actionAbut_DS_Manager.setText(
            QCoreApplication.translate("DedSecWindow", u"Abut DS Manager", None)
        )
        self.actionBackup_Database.setText(
            QCoreApplication.translate("DedSecWindow", u"Backup Database", None)
        )
        self.label.setText("")
        self.label_11.setText(
            QCoreApplication.translate(
                "DedSecWindow",
                u'<html><head/><body><p align="center">MUHIYIDEEN JUMMA MOSQUE</p><p align="center"><span style=" color:#337057;">Dickwella</span></p></body></html>',
                None,
            )
        )
        self.label_10.setText(
            QCoreApplication.translate("DedSecWindow", u"Type Of Money Source", None)
        )
        self.trans_type.setItemText(
            1, QCoreApplication.translate("DedSecWindow", u"Expense", None)
        )
        self.trans_type.setItemText(
            2, QCoreApplication.translate("DedSecWindow", u"Bank Deposit", None)
        )
        self.trans_type.setItemText(
            3, QCoreApplication.translate("DedSecWindow", u"Bank Withdraw", None)
        )

        self.label_5.setText(
            QCoreApplication.translate("DedSecWindow", u"Enter the money", None)
        )
        self.label_4.setText(
            QCoreApplication.translate("DedSecWindow", u"Date of Entry", None)
        )
        self.radioButton_2.setText(
            QCoreApplication.translate("DedSecWindow", u"Cash", None)
        )
        self.radioButton.setText(
            QCoreApplication.translate("DedSecWindow", u"Bank", None)
        )
        self.clear_entry_button.setText(
            QCoreApplication.translate("DedSecWindow", u"Clear", None)
        )
        self.label_2.setText(
            QCoreApplication.translate("DedSecWindow", u"Transaction Type", None)
        )
        self.label_9.setText(
            QCoreApplication.translate(
                "DedSecWindow", u"Write or Select more detail about Transection", None
            )
        )
        self.enter_data_button.setText(
            QCoreApplication.translate("DedSecWindow", u"Enter Data", None)
        )
        self.date_of_entry.setDisplayFormat(
            QCoreApplication.translate("DedSecWindow", u"dd/MM/yyyy", None)
        )
        self.label_3.setText(
            QCoreApplication.translate("DedSecWindow", u"Method of Transaction", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.data_entry_tab),
            QCoreApplication.translate("DedSecWindow", u"Data Entry", None),
        )
        self.label_6.setText(
            QCoreApplication.translate("DedSecWindow", u"Date From", None)
        )
        self.report_date_from.setDisplayFormat(
            QCoreApplication.translate("DedSecWindow", u"dd/MM/yyyy", None)
        )
        self.label_7.setText(
            QCoreApplication.translate("DedSecWindow", u"Date To", None)
        )
        self.report_date_to.setDisplayFormat(
            QCoreApplication.translate("DedSecWindow", u"dd/MM/yyyy", None)
        )
        self.label_12.setText(
            QCoreApplication.translate("DedSecWindow", u"Log Level", None)
        )
        self.comboBox.setItemText(
            0, QCoreApplication.translate("DedSecWindow", u"level 1", None)
        )
        self.comboBox.setItemText(
            1, QCoreApplication.translate("DedSecWindow", u"level 2", None)
        )

        self.print_report_button.setText(
            QCoreApplication.translate("DedSecWindow", u"Print Report", None)
        )
        self.preview_report_button.setText(
            QCoreApplication.translate("DedSecWindow", u"Preview Report", None)
        )
        self.export_pdf_button.setText(
            QCoreApplication.translate("DedSecWindow", u"Export as PDF Report", None)
        )
        self.label_8.setText(
            QCoreApplication.translate(
                "DedSecWindow", u"Select the period for Report generate", None
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.report_gen_tab),
            QCoreApplication.translate("DedSecWindow", u"Report Generator", None),
        )
        self.menuAbout.setTitle(
            QCoreApplication.translate("DedSecWindow", u"Help", None)
        )
        self.menuFile.setTitle(
            QCoreApplication.translate("DedSecWindow", u"File", None)
        )

    # retranslateUi
