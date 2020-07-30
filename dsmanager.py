# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'account_reporter.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import includes_rc

class Ui_DedSecWindow(object):
    def setupUi(self, DedSecWindow):
        if not DedSecWindow.objectName():
            DedSecWindow.setObjectName(u"DedSecWindow")
        DedSecWindow.setWindowModality(Qt.WindowModal)
        DedSecWindow.resize(1011, 934)
        font = QFont()
        font.setFamily(u"Arial Narrow")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        DedSecWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/inc/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        DedSecWindow.setWindowIcon(icon)
        DedSecWindow.setStyleSheet(u"QMainWindow, QWidget#data_entry_tab, QWidget#report_gen_tab{\n"
"	background-color: rgb(255, 255, 255);\n"
"	background-image:url(:/images/inc/blue.png);\n"
"	background-position: center;\n"
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
"}")
        DedSecWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        DedSecWindow.setAnimated(True)
        DedSecWindow.setDocumentMode(False)
        DedSecWindow.setDockNestingEnabled(True)
        self.actionAbut_DS_Manager = QAction(DedSecWindow)
        self.actionAbut_DS_Manager.setObjectName(u"actionAbut_DS_Manager")
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
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(250, 250))
        self.label.setStyleSheet(u"QLabel{\n"
"	border-radius: 25px;\n"
"	padding: 20px;\n"
"	width: 200px;\n"
"	height: 150px; \n"
"}")
        self.label.setPixmap(QPixmap(u":/images/inc/mosque.jpg"))
        self.label.setScaledContents(False)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_8)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamily(u"Times New Roman")
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"color: rgb(113, 108, 255);\n"
"padding:10px;")

        self.horizontalLayout.addWidget(self.label_11)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font2 = QFont()
        font2.setFamily(u"Times New Roman")
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.tabWidget.setFont(font2)
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setElideMode(Qt.ElideLeft)
        self.data_entry_tab = QWidget()
        self.data_entry_tab.setObjectName(u"data_entry_tab")
        self.gridLayout = QGridLayout(self.data_entry_tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(30)
        self.gridLayout.setContentsMargins(80, 40, 20, 10)
        self.label_4 = QLabel(self.data_entry_tab)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setFont(font2)

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 8, 4, 1, 1)

        self.enter_data_button = QPushButton(self.data_entry_tab)
        self.enter_data_button.setObjectName(u"enter_data_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.enter_data_button.sizePolicy().hasHeightForWidth())
        self.enter_data_button.setSizePolicy(sizePolicy2)
        self.enter_data_button.setFont(font2)

        self.gridLayout.addWidget(self.enter_data_button, 8, 3, 1, 1)

        self.more_trans_detail = QLineEdit(self.data_entry_tab)
        self.more_trans_detail.setObjectName(u"more_trans_detail")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.more_trans_detail.sizePolicy().hasHeightForWidth())
        self.more_trans_detail.setSizePolicy(sizePolicy3)
        self.more_trans_detail.setMaximumSize(QSize(300, 16777215))
        font3 = QFont()
        font3.setFamily(u"Times New Roman")
        font3.setPointSize(13)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.more_trans_detail.setFont(font3)
        self.more_trans_detail.setStyleSheet(u"QLineEdit {\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.more_trans_detail.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.more_trans_detail.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.more_trans_detail, 2, 4, 1, 1)

        self.label_9 = QLabel(self.data_entry_tab)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setFont(font2)

        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 8, 2, 1, 1)

        self.method_of_trans = QComboBox(self.data_entry_tab)
        self.method_of_trans.setObjectName(u"method_of_trans")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.method_of_trans.sizePolicy().hasHeightForWidth())
        self.method_of_trans.setSizePolicy(sizePolicy4)
        self.method_of_trans.setMaximumSize(QSize(300, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.method_of_trans.setPalette(palette)
        self.method_of_trans.setFont(font3)
        self.method_of_trans.setStyleSheet(u"QComboBox{\n"
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
"}")

        self.gridLayout.addWidget(self.method_of_trans, 1, 4, 1, 1)

        self.verticalSpacer = QSpacerItem(40, 70, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer, 6, 4, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 8, 0, 1, 1)

        self.clear_entry_button = QPushButton(self.data_entry_tab)
        self.clear_entry_button.setObjectName(u"clear_entry_button")
        sizePolicy2.setHeightForWidth(self.clear_entry_button.sizePolicy().hasHeightForWidth())
        self.clear_entry_button.setSizePolicy(sizePolicy2)
        self.clear_entry_button.setFont(font2)

        self.gridLayout.addWidget(self.clear_entry_button, 8, 1, 1, 1)

        self.label_2 = QLabel(self.data_entry_tab)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setFont(font2)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)

        self.date_of_entry = QDateEdit(self.data_entry_tab)
        self.date_of_entry.setObjectName(u"date_of_entry")
        sizePolicy4.setHeightForWidth(self.date_of_entry.sizePolicy().hasHeightForWidth())
        self.date_of_entry.setSizePolicy(sizePolicy4)
        self.date_of_entry.setMaximumSize(QSize(130, 16777215))
        self.date_of_entry.setFont(font2)
        self.date_of_entry.setStyleSheet(u"QDateEdit{\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QDateEdit:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}")
        self.date_of_entry.setMinimumDateTime(QDateTime(QDate(1767, 9, 14), QTime(0, 0, 0)))
        self.date_of_entry.setCalendarPopup(True)

        self.gridLayout.addWidget(self.date_of_entry, 3, 4, 1, 1)

        self.trans_type = QComboBox(self.data_entry_tab)
        self.trans_type.addItem("")
        self.trans_type.addItem("")
        self.trans_type.addItem("")
        self.trans_type.addItem("")
        self.trans_type.setObjectName(u"trans_type")
        sizePolicy4.setHeightForWidth(self.trans_type.sizePolicy().hasHeightForWidth())
        self.trans_type.setSizePolicy(sizePolicy4)
        self.trans_type.setMaximumSize(QSize(300, 16777215))
        self.trans_type.setFont(font1)
        self.trans_type.setStyleSheet(u"QComboBox{\n"
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
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.trans_type.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.trans_type.setFrame(True)

        self.gridLayout.addWidget(self.trans_type, 0, 4, 1, 1)

        self.label_3 = QLabel(self.data_entry_tab)
        self.label_3.setObjectName(u"label_3")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy5)
        self.label_3.setFont(font2)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_5 = QLabel(self.data_entry_tab)
        self.label_5.setObjectName(u"label_5")
        sizePolicy5.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy5)
        self.label_5.setFont(font2)

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.label_10 = QLabel(self.data_entry_tab)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        self.label_10.setFont(font2)

        self.gridLayout.addWidget(self.label_10, 4, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radioButton_2 = QRadioButton(self.data_entry_tab)
        self.radioButton_2.setObjectName(u"radioButton_2")
        font4 = QFont()
        font4.setFamily(u"Times New Roman")
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(50)
        self.radioButton_2.setFont(font4)

        self.horizontalLayout_2.addWidget(self.radioButton_2)

        self.radioButton = QRadioButton(self.data_entry_tab)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setFont(font4)

        self.horizontalLayout_2.addWidget(self.radioButton)


        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 4, 1, 1)

        self.money = QLineEdit(self.data_entry_tab)
        self.money.setObjectName(u"money")
        sizePolicy4.setHeightForWidth(self.money.sizePolicy().hasHeightForWidth())
        self.money.setSizePolicy(sizePolicy4)
        self.money.setMaximumSize(QSize(200, 16777215))
        self.money.setFont(font3)
        self.money.setStyleSheet(u"QLineEdit {\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.money.setInputMethodHints(Qt.ImhDigitsOnly)
        self.money.setText(u"")
        self.money.setFrame(True)
        self.money.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.money, 5, 4, 1, 1)

        self.tabWidget.addTab(self.data_entry_tab, "")
        self.report_gen_tab = QWidget()
        self.report_gen_tab.setObjectName(u"report_gen_tab")
        self.gridLayout_2 = QGridLayout(self.report_gen_tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setVerticalSpacing(20)
        self.gridLayout_2.setContentsMargins(80, 20, 20, 10)
        self.label_7 = QLabel(self.report_gen_tab)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setFont(font2)

        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 0, 4, 1, 1)

        self.report_date_to = QDateEdit(self.report_gen_tab)
        self.report_date_to.setObjectName(u"report_date_to")
        sizePolicy2.setHeightForWidth(self.report_date_to.sizePolicy().hasHeightForWidth())
        self.report_date_to.setSizePolicy(sizePolicy2)
        self.report_date_to.setFont(font4)
        self.report_date_to.setStyleSheet(u"QDateEdit{\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QDateEdit:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"")
        self.report_date_to.setWrapping(False)
        self.report_date_to.setReadOnly(False)
        self.report_date_to.setProperty("showGroupSeparator", False)
        self.report_date_to.setDateTime(QDateTime(QDate(2020, 1, 1), QTime(0, 0, 0)))
        self.report_date_to.setMinimumDateTime(QDateTime(QDate(2010, 9, 14), QTime(0, 0, 0)))
        self.report_date_to.setCurrentSection(QDateTimeEdit.DaySection)
        self.report_date_to.setCalendarPopup(True)
        self.report_date_to.setTimeSpec(Qt.TimeZone)

        self.gridLayout_2.addWidget(self.report_date_to, 2, 4, 1, 1)

        self.report_date_from = QDateEdit(self.report_gen_tab)
        self.report_date_from.setObjectName(u"report_date_from")
        sizePolicy2.setHeightForWidth(self.report_date_from.sizePolicy().hasHeightForWidth())
        self.report_date_from.setSizePolicy(sizePolicy2)
        self.report_date_from.setFont(font4)
        self.report_date_from.setStyleSheet(u"QDateEdit{\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QDateEdit:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}")
        self.report_date_from.setDateTime(QDateTime(QDate(2020, 1, 1), QTime(0, 0, 0)))
        self.report_date_from.setMinimumDateTime(QDateTime(QDate(2010, 9, 14), QTime(0, 0, 0)))
        self.report_date_from.setMaximumDate(QDate(9999, 11, 30))
        self.report_date_from.setCalendarPopup(True)
        self.report_date_from.setDate(QDate(2020, 1, 1))

        self.gridLayout_2.addWidget(self.report_date_from, 1, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.label_6 = QLabel(self.report_gen_tab)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setFont(font2)

        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 4, 0, 1, 1)

        self.preview_report_button = QPushButton(self.report_gen_tab)
        self.preview_report_button.setObjectName(u"preview_report_button")
        sizePolicy2.setHeightForWidth(self.preview_report_button.sizePolicy().hasHeightForWidth())
        self.preview_report_button.setSizePolicy(sizePolicy2)
        self.preview_report_button.setFont(font2)

        self.gridLayout_2.addWidget(self.preview_report_button, 5, 2, 1, 1)

        self.label_8 = QLabel(self.report_gen_tab)
        self.label_8.setObjectName(u"label_8")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy6)
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"")
        self.label_8.setMargin(10)

        self.gridLayout_2.addWidget(self.label_8, 0, 2, 1, 2)

        self.export_pdf_button = QPushButton(self.report_gen_tab)
        self.export_pdf_button.setObjectName(u"export_pdf_button")
        sizePolicy2.setHeightForWidth(self.export_pdf_button.sizePolicy().hasHeightForWidth())
        self.export_pdf_button.setSizePolicy(sizePolicy2)
        self.export_pdf_button.setFont(font2)
        self.export_pdf_button.setLayoutDirection(Qt.LeftToRight)
        self.export_pdf_button.setFlat(False)

        self.gridLayout_2.addWidget(self.export_pdf_button, 5, 4, 1, 1)

        self.print_report_button = QPushButton(self.report_gen_tab)
        self.print_report_button.setObjectName(u"print_report_button")
        sizePolicy2.setHeightForWidth(self.print_report_button.sizePolicy().hasHeightForWidth())
        self.print_report_button.setSizePolicy(sizePolicy2)
        self.print_report_button.setFont(font2)

        self.gridLayout_2.addWidget(self.print_report_button, 5, 3, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_6, 5, 0, 1, 1)

        self.label_12 = QLabel(self.report_gen_tab)
        self.label_12.setObjectName(u"label_12")
        sizePolicy1.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)
        font5 = QFont()
        font5.setFamily(u"Times New Roman")
        font5.setPointSize(11)
        self.label_12.setFont(font5)

        self.gridLayout_2.addWidget(self.label_12, 3, 0, 1, 1)

        self.comboBox = QComboBox(self.report_gen_tab)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy2.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy2)
        self.comboBox.setFont(font5)
        self.comboBox.setStyleSheet(u"QComboBox{\n"
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
"}")

        self.gridLayout_2.addWidget(self.comboBox, 3, 4, 1, 1)

        self.tabWidget.addTab(self.report_gen_tab, "")

        self.verticalLayout_3.addWidget(self.tabWidget)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        DedSecWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(DedSecWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1011, 26))
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
        DedSecWindow.setWindowTitle(QCoreApplication.translate("DedSecWindow", u"DS Manager", None))
        self.actionAbut_DS_Manager.setText(QCoreApplication.translate("DedSecWindow", u"Abut DS Manager", None))
        self.actionBackup_Database.setText(QCoreApplication.translate("DedSecWindow", u"Backup Database", None))
        self.label.setText("")
        self.label_11.setText(QCoreApplication.translate("DedSecWindow", u"<html><head/><body><p>MUHIYIDEEN JUMMA MOSQUE</p><p align=\"center\">Dickwella</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("DedSecWindow", u"Date of Entry", None))
        self.enter_data_button.setText(QCoreApplication.translate("DedSecWindow", u"Enter Data", None))
        self.label_9.setText(QCoreApplication.translate("DedSecWindow", u"Write or Select more detail about Transection", None))
        self.clear_entry_button.setText(QCoreApplication.translate("DedSecWindow", u"Clear", None))
        self.label_2.setText(QCoreApplication.translate("DedSecWindow", u"Transaction Type", None))
        self.date_of_entry.setDisplayFormat(QCoreApplication.translate("DedSecWindow", u"dd/MM/yyyy", None))
        self.trans_type.setItemText(0, QCoreApplication.translate("DedSecWindow", u"Income", None))
        self.trans_type.setItemText(1, QCoreApplication.translate("DedSecWindow", u"Expense", None))
        self.trans_type.setItemText(2, QCoreApplication.translate("DedSecWindow", u"Bank Deposite", None))
        self.trans_type.setItemText(3, QCoreApplication.translate("DedSecWindow", u"Bank Withdraw", None))

        self.label_3.setText(QCoreApplication.translate("DedSecWindow", u"Method of Transaction", None))
        self.label_5.setText(QCoreApplication.translate("DedSecWindow", u"Enter the money", None))
        self.label_10.setText(QCoreApplication.translate("DedSecWindow", u"Type Of Money Source", None))
        self.radioButton_2.setText(QCoreApplication.translate("DedSecWindow", u"Cash", None))
        self.radioButton.setText(QCoreApplication.translate("DedSecWindow", u"Bank", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.data_entry_tab), QCoreApplication.translate("DedSecWindow", u"Data Entry", None))
        self.label_7.setText(QCoreApplication.translate("DedSecWindow", u"Date To", None))
        self.report_date_to.setDisplayFormat(QCoreApplication.translate("DedSecWindow", u"dd/MM/yyyy", None))
        self.report_date_from.setDisplayFormat(QCoreApplication.translate("DedSecWindow", u"dd/MM/yyyy", None))
        self.label_6.setText(QCoreApplication.translate("DedSecWindow", u"Date From", None))
        self.preview_report_button.setText(QCoreApplication.translate("DedSecWindow", u"Preview Report", None))
        self.label_8.setText(QCoreApplication.translate("DedSecWindow", u"Select the period for Report generate", None))
        self.export_pdf_button.setText(QCoreApplication.translate("DedSecWindow", u"Export as PDF Report", None))
        self.print_report_button.setText(QCoreApplication.translate("DedSecWindow", u"Print Report", None))
        self.label_12.setText(QCoreApplication.translate("DedSecWindow", u"Log Level", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("DedSecWindow", u"level 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("DedSecWindow", u"level 2", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.report_gen_tab), QCoreApplication.translate("DedSecWindow", u"Report Generator", None))
        self.menuAbout.setTitle(QCoreApplication.translate("DedSecWindow", u"Help", None))
        self.menuFile.setTitle(QCoreApplication.translate("DedSecWindow", u"File", None))
    # retranslateUi

