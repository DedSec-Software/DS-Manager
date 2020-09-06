# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pdfviewer.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from os.path import abspath
from PySide2.QtCore import QCoreApplication, QMetaObject, QSize, QUrl
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QWidget, QVBoxLayout, QSizePolicy
from PySide2.QtWebEngineWidgets import QWebEngineView as QWebView
from PySide2.QtWebEngineWidgets import QWebEngineSettings

import includes_rc


class Ui_PDFViewer(object):
    def setupUi(self, PDFViewer):
        if not PDFViewer.objectName():
            PDFViewer.setObjectName(u"PDFViewer")
        PDFViewer.resize(820, 652)
        icon = QIcon()
        icon.addFile(u":/icons/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        PDFViewer.setWindowIcon(icon)
        self.centralwidget = QWidget(PDFViewer)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.webView = QWebView(self.centralwidget)
        self.webView.setObjectName(u"webView")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webView.sizePolicy().hasHeightForWidth())
        self.webView.setSizePolicy(sizePolicy)
        self.webView.setProperty("url", QUrl(u""))

        self.verticalLayout.addWidget(self.webView)

        PDFViewer.setCentralWidget(self.centralwidget)

        self.retranslateUi(PDFViewer)

        QMetaObject.connectSlotsByName(PDFViewer)

    # setupUi

    def retranslateUi(self, PDFViewer):
        PDFViewer.setWindowTitle(
            QCoreApplication.translate("PDFViewer", u"MainWindow", None)
        )

    # retranslateUi
