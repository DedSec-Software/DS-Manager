# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (
    QCoreApplication,
    QMetaObject,
    QRect,
    QSize,
    Qt,
)
from PySide2.QtGui import (
    QFont,
    QPixmap,
)
from PySide2.QtWidgets import *

import includes_rc


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(767, 537)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMaximumSize(QSize(767, 537))
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-20, -10, 800, 641))
        self.frame.setMaximumSize(QSize(800, 650))
        self.frame.setStyleSheet(
            u"QFrame{\n" "	\n" "	background-color: rgb(255, 255, 255);\n" "}"
        )
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Plain)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 20, 61, 71))
        self.label.setPixmap(QPixmap(u":/icons/icon.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(150, 40, 531, 31))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(
            u"color:qlineargradient(spread:pad, x1:0.532552, y1:0, x2:0.522, y2:0.926136, stop:0.0199005 rgba(70, 14, 184, 255), stop:0.965174 rgba(14, 18, 117, 255))"
        )
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(300, 160, 291, 51))
        font1 = QFont()
        font1.setFamily(u"Tahoma")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_3.setFont(font1)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(280, 90, 231, 31))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(
            u"color:qlineargradient(spread:pad, x1:0.532552, y1:0, x2:0.522, y2:0.932, stop:0.308458 rgba(114, 80, 184, 255), stop:0.965174 rgba(31, 88, 255, 211))"
        )
        self.label_4.setFrameShape(QFrame.NoFrame)
        self.label_4.setFrameShadow(QFrame.Plain)
        self.label_4.setWordWrap(False)
        self.label_4.setMargin(0)
        self.label_4.setIndent(0)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(170, 140, 91, 91))
        self.label_5.setStyleSheet(u"QLabel{\n" "	border-radius: 60px;\n" "}")
        self.label_5.setFrameShape(QFrame.NoFrame)
        self.label_5.setFrameShadow(QFrame.Plain)
        self.label_5.setPixmap(QPixmap(u":/images/zumair.jpg"))
        self.label_5.setScaledContents(True)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(300, 270, 401, 51))
        self.label_6.setFont(font1)
        self.buttonBox = QDialogButtonBox(self.frame)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(650, 490, 111, 32))
        font2 = QFont()
        font2.setFamily(u"Candara")
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setWeight(75)
        self.buttonBox.setFont(font2)
        self.buttonBox.setStyleSheet(
            u"\n"
            "background-color:qlineargradient(spread:pad, x1:0.532552, y1:0, x2:0.522, y2:0.932, stop:0 rgba(128, 101, 184, 255), stop:0.487562 rgba(131, 101, 220, 233), stop:0.965174 rgba(77, 123, 255, 211));\n"
            "width:110%;\n"
            "height:40%;\n"
            "color:white;\n"
            "border-radius:8px;\n"
            "\n"
            "font-size:10;\n"
            ""
        )
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(170, 250, 91, 91))
        self.label_7.setStyleSheet(u"QLabel>qpixmap{\n" "	border-radius: 50%;\n" "}")
        self.label_7.setPixmap(QPixmap(u":/images/pakee.png"))
        self.label_7.setScaledContents(True)
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(300, 390, 401, 51))
        self.label_8.setFont(font1)
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(170, 360, 91, 91))
        self.label_9.setStyleSheet(u"QLabel>qpixmap{\n" "	border-radius: 50%;\n" "}")
        self.label_9.setPixmap(QPixmap(u":/images/new.png"))
        self.label_9.setScaledContents(True)

        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.buttonBox.accepted.connect(Dialog.accept)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate("Dialog", u"About DS Manager", None)
        )
        self.label.setText("")
        self.label_2.setText(
            QCoreApplication.translate(
                "Dialog", u"DedSec Manager - Copyright \u00a9 2020", None
            )
        )
        self.label_3.setText(
            QCoreApplication.translate(
                "Dialog", u"Mohamed Zumair - Core Developer", None
            )
        )
        self.label_4.setText(
            QCoreApplication.translate("Dialog", u"Team Members", None)
        )
        self.label_5.setText("")
        self.label_6.setText(
            QCoreApplication.translate(
                "Dialog", u"Pakeetharan Balasubramaniam - Database Admin", None
            )
        )
        self.label_7.setText("")
        self.label_8.setText(
            QCoreApplication.translate(
                "Dialog", u"Himasha Gunasena - UI/UX Designer", None
            )
        )
        self.label_9.setText("")

    # retranslateUi
