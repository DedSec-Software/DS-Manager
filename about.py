# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(800, 550)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMaximumSize(QSize(800, 550))
        icon = QIcon()
        icon.addFile(u":/icons/inc/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 801, 551))
        self.frame.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Plain)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 10, 201, 191))
        self.label.setPixmap(QPixmap(u":/icons/inc/icon.ico"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(210, 50, 441, 31))
        font = QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(300, 160, 291, 51))
        font1 = QFont()
        font1.setFamily(u"Times New Roman")
        font1.setPointSize(10)
        self.label_3.setFont(font1)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(320, 100, 201, 31))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QFrame.NoFrame)
        self.label_4.setFrameShadow(QFrame.Plain)
        self.label_4.setWordWrap(False)
        self.label_4.setMargin(0)
        self.label_4.setIndent(0)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(190, 140, 91, 91))
        self.label_5.setStyleSheet(u"QLabel{\n"
"	border-radius: 60px;\n"
"}")
        self.label_5.setFrameShape(QFrame.NoFrame)
        self.label_5.setFrameShadow(QFrame.Plain)
        self.label_5.setPixmap(QPixmap(u":/images/inc/zumair.jpg"))
        self.label_5.setScaledContents(True)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(300, 270, 401, 51))
        self.label_6.setFont(font1)
        self.buttonBox = QDialogButtonBox(self.frame)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(650, 490, 111, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(190, 250, 91, 91))
        self.label_7.setStyleSheet(u"QLabel>qpixmap{\n"
"	border-radius: 50%;\n"
"}")
        self.label_7.setPixmap(QPixmap(u"inc/pakee.png"))
        self.label_7.setScaledContents(True)
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(300, 390, 401, 51))
        self.label_8.setFont(font1)
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(190, 370, 91, 91))
        self.label_9.setStyleSheet(u"QLabel>qpixmap{\n"
"	border-radius: 50%;\n"
"}")
        self.label_9.setPixmap(QPixmap(u":/images/inc/panchali.png"))
        self.label_9.setScaledContents(True)

        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.buttonBox.accepted.connect(Dialog.accept)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"About DS Manager", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"DedSec Manager - Copyright \u00a9 2020", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Mohamed Zumair - Core Developer", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Team Members", None))
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Pakeetharan Balasubramaniam - Database Admin", None))
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Himasha gunasena - UI/UX Designer", None))
        self.label_9.setText("")
    # retranslateUi

