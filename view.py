#  Copyright (C) 2020  Mohamed Zumair <mhdzumair@gmail.com>
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.

from PySide2.QtCore import QSize, QUrl
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QMainWindow, QMessageBox, QDialog, QButtonGroup
from about import Ui_About
from dsmanager import Ui_DsManager
from model import Model
from pdfviewer import Ui_PDFViewer


class View(QMainWindow, Ui_DsManager):
    def __init__(self, *args, **kwargs):
        super(View, self).__init__(*args, **kwargs)
        self.setupUi(self)

    def setupUi(self, DsManager):
        super(View, self).setupUi(DsManager)
        self.source_btn_group = QButtonGroup(self)
        self.reversed_entry_btn_group = QButtonGroup(self)
        self.source_btn_group.setExclusive(True)
        self.reversed_entry_btn_group.setExclusive(True)
        self.source_btn_group.addButton(self.cash_radio, 1)
        self.source_btn_group.addButton(self.main_radio, 2)
        self.source_btn_group.addButton(self.building_radio, 3)
        self.reversed_entry_btn_group.addButton(self.reversed_entry_increase, 1)
        self.reversed_entry_btn_group.addButton(self.reversed_entry_decrease, 2)
        self.cheque_label.hide()
        self.cheque_number.hide()

    def view_pdf(self, pdf_js, pdf_file_name):
        new_window = QMainWindow(self)
        pdf_viewer = Ui_PDFViewer()
        pdf_viewer.setupUi(new_window)
        pdf_url = QUrl.fromLocalFile(pdf_js)
        pdf_url.setQuery("file=" + pdf_file_name)
        pdf_viewer.webView.load(pdf_url)
        new_window.show()

    @classmethod
    def show_about_ds(cls):
        dialog = QDialog()
        about = Ui_About()
        about.setupUi(dialog)
        dialog.exec_()

    @classmethod
    def show_message(cls, message: str, logo: str):
        msg = QMessageBox()
        icon = QIcon()
        icon.addFile(u"inc/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        msg.setWindowIcon(icon)
        if logo == "error":
            msg.setIcon(QMessageBox.Critical)
        elif logo == "info":
            msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle(logo)
        msg.exec_()

    def closeEvent(self, event):
        model = Model()
        model.close_connection()
        event.accept()
