# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dsmanager.ui'
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


class Ui_DsManager(object):
    def setupUi(self, DsManager):
        if not DsManager.objectName():
            DsManager.setObjectName(u"DsManager")
        DsManager.setWindowModality(Qt.WindowModal)
        DsManager.resize(1156, 934)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DsManager.sizePolicy().hasHeightForWidth())
        DsManager.setSizePolicy(sizePolicy)
        DsManager.setMinimumSize(QSize(0, 800))
        font = QFont()
        font.setFamily(u"Arial Narrow")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        DsManager.setFont(font)
        icon = QIcon()
        icon.addFile(u"inc/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        DsManager.setWindowIcon(icon)
        DsManager.setStyleSheet(
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
        DsManager.setToolButtonStyle(Qt.ToolButtonIconOnly)
        DsManager.setAnimated(True)
        DsManager.setDocumentMode(False)
        DsManager.setDockNestingEnabled(True)
        self.actionAbut_DS_Manager = QAction(DsManager)
        self.actionAbut_DS_Manager.setObjectName(u"actionAbut_DS_Manager")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbut_DS_Manager.setIcon(icon1)
        self.actionAbut_DS_Manager.setShortcutContext(Qt.WidgetShortcut)
        self.actionAbut_DS_Manager.setMenuRole(QAction.TextHeuristicRole)
        self.actionBackup_Database = QAction(DsManager)
        self.actionBackup_Database.setObjectName(u"actionBackup_Database")
        font1 = QFont()
        font1.setFamily(u"Microsoft YaHei UI")
        font1.setPointSize(8)
        self.actionBackup_Database.setFont(font1)
        self.actionRestore_Database = QAction(DsManager)
        self.actionRestore_Database.setObjectName(u"actionRestore_Database")
        self.centralwidget = QWidget(DsManager)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth()
        )
        self.centralwidget.setSizePolicy(sizePolicy)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMaximumSize(QSize(164, 164))
        self.label.setStyleSheet(u"")
        self.label.setTextFormat(Qt.PlainText)
        self.label.setPixmap(QPixmap(u":/icons/home_logo.png"))
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
        font2 = QFont()
        font2.setFamily(u"Tahoma")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setWeight(75)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.label_11.setFont(font2)
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
        font3 = QFont()
        font3.setFamily(u"Microsoft YaHei UI")
        font3.setPointSize(9)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setWeight(75)
        self.tabWidget.setFont(font3)
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
        font4 = QFont()
        font4.setBold(False)
        font4.setWeight(50)
        self.data_entry_tab.setFont(font4)
        self.gridLayout = QGridLayout(self.data_entry_tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(30)
        self.gridLayout.setContentsMargins(80, 40, 20, 10)
        self.label_13 = QLabel(self.data_entry_tab)
        self.label_13.setObjectName(u"label_13")
        sizePolicy2.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy2)
        font5 = QFont()
        font5.setFamily(u"Microsoft YaHei UI")
        font5.setPointSize(11)
        font5.setBold(False)
        font5.setWeight(50)
        font5.setStyleStrategy(QFont.PreferAntialias)
        self.label_13.setFont(font5)

        self.gridLayout.addWidget(self.label_13, 8, 1, 1, 1)

        self.label_10 = QLabel(self.data_entry_tab)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)
        font6 = QFont()
        font6.setFamily(u"Microsoft YaHei UI")
        font6.setPointSize(11)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setWeight(50)
        font6.setStrikeOut(False)
        font6.setStyleStrategy(QFont.PreferAntialias)
        self.label_10.setFont(font6)
        self.label_10.setStyleSheet(u"")

        self.gridLayout.addWidget(self.label_10, 5, 1, 1, 1)

        self.clear_entry_button = QPushButton(self.data_entry_tab)
        self.clear_entry_button.setObjectName(u"clear_entry_button")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.clear_entry_button.sizePolicy().hasHeightForWidth()
        )
        self.clear_entry_button.setSizePolicy(sizePolicy3)
        font7 = QFont()
        font7.setFamily(u"Microsoft YaHei UI")
        font7.setPointSize(11)
        font7.setBold(True)
        font7.setItalic(False)
        font7.setWeight(75)
        font7.setKerning(True)
        self.clear_entry_button.setFont(font7)
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

        self.gridLayout.addWidget(self.clear_entry_button, 12, 2, 1, 1)

        self.enter_data_button = QPushButton(self.data_entry_tab)
        self.enter_data_button.setObjectName(u"enter_data_button")
        sizePolicy3.setHeightForWidth(
            self.enter_data_button.sizePolicy().hasHeightForWidth()
        )
        self.enter_data_button.setSizePolicy(sizePolicy3)
        font8 = QFont()
        font8.setFamily(u"Microsoft YaHei UI")
        font8.setPointSize(11)
        font8.setBold(True)
        font8.setItalic(False)
        font8.setWeight(75)
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

        self.gridLayout.addWidget(self.enter_data_button, 12, 4, 1, 1)

        self.label_3 = QLabel(self.data_entry_tab)
        self.label_3.setObjectName(u"label_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy4)
        self.label_3.setFont(font6)

        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)

        self.more_trans_detail = QLineEdit(self.data_entry_tab)
        self.more_trans_detail.setObjectName(u"more_trans_detail")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(
            self.more_trans_detail.sizePolicy().hasHeightForWidth()
        )
        self.more_trans_detail.setSizePolicy(sizePolicy5)
        self.more_trans_detail.setMaximumSize(QSize(300, 16777215))
        font9 = QFont()
        font9.setFamily(u"Microsoft YaHei UI")
        font9.setPointSize(11)
        font9.setBold(False)
        font9.setItalic(False)
        font9.setWeight(50)
        self.more_trans_detail.setFont(font9)
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

        self.method_of_trans = QComboBox(self.data_entry_tab)
        self.method_of_trans.setObjectName(u"method_of_trans")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(
            self.method_of_trans.sizePolicy().hasHeightForWidth()
        )
        self.method_of_trans.setSizePolicy(sizePolicy6)
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
        font10 = QFont()
        font10.setFamily(u"Microsoft YaHei UI")
        font10.setPointSize(12)
        font10.setBold(False)
        font10.setItalic(False)
        font10.setWeight(50)
        self.method_of_trans.setFont(font10)
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

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.cash_radio = QRadioButton(self.data_entry_tab)
        self.cash_radio.setObjectName(u"cash_radio")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.cash_radio.sizePolicy().hasHeightForWidth())
        self.cash_radio.setSizePolicy(sizePolicy7)
        self.cash_radio.setMinimumSize(QSize(80, 0))
        self.cash_radio.setFont(font9)

        self.horizontalLayout_2.addWidget(self.cash_radio)

        self.main_radio = QRadioButton(self.data_entry_tab)
        self.main_radio.setObjectName(u"main_radio")
        self.main_radio.setMinimumSize(QSize(150, 0))
        self.main_radio.setFont(font9)

        self.horizontalLayout_2.addWidget(self.main_radio)

        self.building_radio = QRadioButton(self.data_entry_tab)
        self.building_radio.setObjectName(u"building_radio")
        self.building_radio.setMinimumSize(QSize(175, 0))
        font11 = QFont()
        font11.setFamily(u"Microsoft YaHei UI")
        font11.setPointSize(11)
        self.building_radio.setFont(font11)

        self.horizontalLayout_2.addWidget(self.building_radio)

        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 7, 1, 1)

        self.label_9 = QLabel(self.data_entry_tab)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setFont(font6)

        self.gridLayout.addWidget(self.label_9, 3, 1, 1, 4)

        self.label_4 = QLabel(self.data_entry_tab)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setFont(font6)
        self.label_4.setStyleSheet(u"")

        self.gridLayout.addWidget(self.label_4, 4, 1, 1, 1)

        self.label_5 = QLabel(self.data_entry_tab)
        self.label_5.setObjectName(u"label_5")
        sizePolicy4.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy4)
        self.label_5.setFont(font6)

        self.gridLayout.addWidget(self.label_5, 7, 1, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(
            100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout.addItem(self.horizontalSpacer_9, 12, 3, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(
            100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout.addItem(self.horizontalSpacer_8, 12, 7, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.reversed_entry_increase = QCheckBox(self.data_entry_tab)
        self.reversed_entry_increase.setObjectName(u"reversed_entry_increase")
        self.reversed_entry_increase.setFont(font11)

        self.horizontalLayout_4.addWidget(self.reversed_entry_increase)

        self.reversed_entry_decrease = QCheckBox(self.data_entry_tab)
        self.reversed_entry_decrease.setObjectName(u"reversed_entry_decrease")
        self.reversed_entry_decrease.setFont(font11)

        self.horizontalLayout_4.addWidget(self.reversed_entry_decrease)

        self.gridLayout.addLayout(self.horizontalLayout_4, 8, 7, 1, 1)

        self.date_of_entry = QDateEdit(self.data_entry_tab)
        self.date_of_entry.setObjectName(u"date_of_entry")
        sizePolicy6.setHeightForWidth(
            self.date_of_entry.sizePolicy().hasHeightForWidth()
        )
        self.date_of_entry.setSizePolicy(sizePolicy6)
        self.date_of_entry.setMaximumSize(QSize(150, 16777215))
        self.date_of_entry.setFont(font9)
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

        self.money = QLineEdit(self.data_entry_tab)
        self.money.setObjectName(u"money")
        sizePolicy6.setHeightForWidth(self.money.sizePolicy().hasHeightForWidth())
        self.money.setSizePolicy(sizePolicy6)
        self.money.setMaximumSize(QSize(200, 16777215))
        self.money.setFont(font9)
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

        self.gridLayout.addWidget(self.money, 7, 7, 1, 1)

        self.label_2 = QLabel(self.data_entry_tab)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setFont(font6)

        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        self.trans_type = QComboBox(self.data_entry_tab)
        self.trans_type.addItem(u"Income")
        self.trans_type.addItem("")
        self.trans_type.addItem("")
        self.trans_type.addItem("")
        self.trans_type.setObjectName(u"trans_type")
        sizePolicy6.setHeightForWidth(self.trans_type.sizePolicy().hasHeightForWidth())
        self.trans_type.setSizePolicy(sizePolicy6)
        self.trans_type.setMaximumSize(QSize(300, 16777215))
        self.trans_type.setFont(font9)
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

        self.cheque_label = QLabel(self.data_entry_tab)
        self.cheque_label.setObjectName(u"cheque_label")
        self.cheque_label.setFont(font11)

        self.gridLayout.addWidget(self.cheque_label, 6, 1, 1, 1)

        self.cheque_number = QLineEdit(self.data_entry_tab)
        self.cheque_number.setObjectName(u"cheque_number")
        sizePolicy6.setHeightForWidth(
            self.cheque_number.sizePolicy().hasHeightForWidth()
        )
        self.cheque_number.setSizePolicy(sizePolicy6)
        self.cheque_number.setMaximumSize(QSize(200, 16777215))
        self.cheque_number.setFont(font11)
        self.cheque_number.setStyleSheet(
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

        self.gridLayout.addWidget(self.cheque_number, 6, 7, 1, 1)

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
        self.label_6.setFont(font9)

        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)

        self.report_date_from = QDateEdit(self.report_gen_tab)
        self.report_date_from.setObjectName(u"report_date_from")
        sizePolicy3.setHeightForWidth(
            self.report_date_from.sizePolicy().hasHeightForWidth()
        )
        self.report_date_from.setSizePolicy(sizePolicy3)
        font12 = QFont()
        font12.setFamily(u"Microsoft YaHei UI")
        font12.setPointSize(11)
        font12.setBold(False)
        font12.setItalic(False)
        font12.setUnderline(False)
        font12.setWeight(50)
        self.report_date_from.setFont(font12)
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
        self.label_7.setFont(font9)

        self.gridLayout_2.addWidget(self.label_7, 4, 0, 1, 1)

        self.report_date_to = QDateEdit(self.report_gen_tab)
        self.report_date_to.setObjectName(u"report_date_to")
        sizePolicy3.setHeightForWidth(
            self.report_date_to.sizePolicy().hasHeightForWidth()
        )
        self.report_date_to.setSizePolicy(sizePolicy3)
        self.report_date_to.setFont(font12)
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
        font13 = QFont()
        font13.setFamily(u"Microsoft YaHei UI")
        font13.setPointSize(11)
        font13.setBold(False)
        font13.setWeight(50)
        self.label_12.setFont(font13)

        self.gridLayout_2.addWidget(self.label_12, 6, 0, 1, 1)

        self.comboBox = QComboBox(self.report_gen_tab)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy3.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy3)
        self.comboBox.setMinimumSize(QSize(70, 0))
        self.comboBox.setFont(font13)
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

        self.preview_report_button = QPushButton(self.report_gen_tab)
        self.preview_report_button.setObjectName(u"preview_report_button")
        sizePolicy3.setHeightForWidth(
            self.preview_report_button.sizePolicy().hasHeightForWidth()
        )
        self.preview_report_button.setSizePolicy(sizePolicy3)
        self.preview_report_button.setMinimumSize(QSize(157, 0))
        self.preview_report_button.setFont(font8)
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
        sizePolicy3.setHeightForWidth(
            self.export_pdf_button.sizePolicy().hasHeightForWidth()
        )
        self.export_pdf_button.setSizePolicy(sizePolicy3)
        self.export_pdf_button.setMinimumSize(QSize(208, 0))
        self.export_pdf_button.setFont(font8)
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
        sizePolicy7.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy7)
        font14 = QFont()
        font14.setFamily(u"Microsoft YaHei UI")
        font14.setPointSize(15)
        font14.setBold(False)
        font14.setItalic(False)
        font14.setWeight(50)
        self.label_8.setFont(font14)
        self.label_8.setStyleSheet(
            u"background-color:rgba(0,0,0,0%);\n" "color:rgb(35, 93, 74)"
        )
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setMargin(10)

        self.gridLayout_2.addWidget(self.label_8, 0, 1, 1, 3)

        self.print_report_button = QPushButton(self.report_gen_tab)
        self.print_report_button.setObjectName(u"print_report_button")
        sizePolicy3.setHeightForWidth(
            self.print_report_button.sizePolicy().hasHeightForWidth()
        )
        self.print_report_button.setSizePolicy(sizePolicy3)
        self.print_report_button.setMinimumSize(QSize(140, 0))
        self.print_report_button.setFont(font8)
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

        self.tabWidget.addTab(self.report_gen_tab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        DsManager.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(DsManager)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1156, 24))
        font15 = QFont()
        font15.setFamily(u"Candara")
        font15.setBold(True)
        font15.setWeight(75)
        self.menubar.setFont(font15)
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
        DsManager.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(DsManager)
        self.statusbar.setObjectName(u"statusbar")
        DsManager.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuAbout.addAction(self.actionAbut_DS_Manager)
        self.menuFile.addAction(self.actionBackup_Database)
        self.menuFile.addAction(self.actionRestore_Database)

        self.retranslateUi(DsManager)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(DsManager)

    # setupUi

    def retranslateUi(self, DsManager):
        DsManager.setWindowTitle(
            QCoreApplication.translate("DsManager", u"DS Manager", None)
        )
        self.actionAbut_DS_Manager.setText(
            QCoreApplication.translate("DsManager", u"Abut DS Manager", None)
        )
        self.actionBackup_Database.setText(
            QCoreApplication.translate("DsManager", u"Backup Database", None)
        )
        self.actionRestore_Database.setText(
            QCoreApplication.translate("DsManager", u"Restore Database", None)
        )
        self.label.setText("")
        self.label_11.setText(
            QCoreApplication.translate(
                "DsManager",
                u'<html><head/><body><p align="center">MUHIYIDEEN JUMMA MOSQUE</p><p align="center"><span style=" color:#337057;">Dickwella</span></p></body></html>',
                None,
            )
        )
        self.label_13.setText(
            QCoreApplication.translate("DsManager", u"Reversed Entry", None)
        )
        self.label_10.setText(
            QCoreApplication.translate("DsManager", u"Type Of Money Source", None)
        )
        self.clear_entry_button.setText(
            QCoreApplication.translate("DsManager", u"Clear", None)
        )
        # if QT_CONFIG(shortcut)
        self.clear_entry_button.setShortcut(
            QCoreApplication.translate("DsManager", u"Esc", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.enter_data_button.setText(
            QCoreApplication.translate("DsManager", u"Enter Data", None)
        )
        # if QT_CONFIG(shortcut)
        self.enter_data_button.setShortcut(
            QCoreApplication.translate("DsManager", u"Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_3.setText(
            QCoreApplication.translate("DsManager", u"Method of Transaction", None)
        )
        self.cash_radio.setText(QCoreApplication.translate("DsManager", u"Cash", None))
        self.main_radio.setText(
            QCoreApplication.translate("DsManager", u"Main Account", None)
        )
        self.building_radio.setText(
            QCoreApplication.translate("DsManager", u"Building Account", None)
        )
        self.label_9.setText(
            QCoreApplication.translate(
                "DsManager", u"Write or Select more detail about Transection", None
            )
        )
        self.label_4.setText(
            QCoreApplication.translate("DsManager", u"Date of Entry", None)
        )
        self.label_5.setText(
            QCoreApplication.translate("DsManager", u"Enter the money", None)
        )
        self.reversed_entry_increase.setText(
            QCoreApplication.translate("DsManager", u"Increase", None)
        )
        self.reversed_entry_decrease.setText(
            QCoreApplication.translate("DsManager", u"Decrease", None)
        )
        self.date_of_entry.setDisplayFormat(
            QCoreApplication.translate("DsManager", u"dd/MM/yyyy", None)
        )
        self.label_2.setText(
            QCoreApplication.translate("DsManager", u"Transaction Type", None)
        )
        self.trans_type.setItemText(
            1, QCoreApplication.translate("DsManager", u"Expense", None)
        )
        self.trans_type.setItemText(
            2, QCoreApplication.translate("DsManager", u"Bank Deposit", None)
        )
        self.trans_type.setItemText(
            3, QCoreApplication.translate("DsManager", u"Bank Withdraw", None)
        )

        self.cheque_label.setText(
            QCoreApplication.translate("DsManager", u"Cheque Number", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.data_entry_tab),
            QCoreApplication.translate("DsManager", u"Data Entry", None),
        )
        self.label_6.setText(
            QCoreApplication.translate("DsManager", u"Date From", None)
        )
        self.report_date_from.setDisplayFormat(
            QCoreApplication.translate("DsManager", u"dd/MM/yyyy", None)
        )
        self.label_7.setText(QCoreApplication.translate("DsManager", u"Date To", None))
        self.report_date_to.setDisplayFormat(
            QCoreApplication.translate("DsManager", u"dd/MM/yyyy", None)
        )
        self.label_12.setText(
            QCoreApplication.translate("DsManager", u"Report Level", None)
        )
        self.comboBox.setItemText(
            0, QCoreApplication.translate("DsManager", u"1", None)
        )
        self.comboBox.setItemText(
            1, QCoreApplication.translate("DsManager", u"2", None)
        )

        self.preview_report_button.setText(
            QCoreApplication.translate("DsManager", u"Preview Report", None)
        )
        self.export_pdf_button.setText(
            QCoreApplication.translate("DsManager", u"Export as PDF Report", None)
        )
        self.label_8.setText(
            QCoreApplication.translate(
                "DsManager", u"Select the period for report generate", None
            )
        )
        self.print_report_button.setText(
            QCoreApplication.translate("DsManager", u"Print Report", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.report_gen_tab),
            QCoreApplication.translate("DsManager", u"Report Generator", None),
        )
        self.menuAbout.setTitle(QCoreApplication.translate("DsManager", u"Help", None))
        self.menuFile.setTitle(QCoreApplication.translate("DsManager", u"File", None))

    # retranslateUi
