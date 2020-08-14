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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(820, 652)
        icon = QIcon()
        icon.addFile(u":/icons/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
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
        self.pdf_js = abspath("inc/pdfjs/web/viewer.html")
        self.pdf_path = None
        self.pdf_url = None

        self.settings = QWebEngineSettings.globalSettings()
        self.settings.setAttribute(
            QWebEngineSettings.LocalContentCanAccessFileUrls, True
        )
        self.settings.setAttribute(
            QWebEngineSettings.LocalContentCanAccessRemoteUrls, True
        )
        self.settings.setAttribute(QWebEngineSettings.LocalStorageEnabled, True)
        self.settings.setAttribute(QWebEngineSettings.JavascriptEnabled, True)

        self.verticalLayout.addWidget(self.webView)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"Ds Manager - Pdf viewer", None)
        )

    # retranslateUi

    def set_pdf(self, pdf_path):
        self.pdf_path = abspath(pdf_path)

    def show_pdf(self, MainWindow):
        self.pdf_url = QUrl.fromLocalFile(self.pdf_js)
        self.pdf_url.setQuery("file=" + self.pdf_path)
        self.webView.load(self.pdf_url)
        MainWindow.show()
