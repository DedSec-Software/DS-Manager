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

from PySide2.QtWidgets import QCompleter, QFileDialog
from PySide2.QtCore import QDate, Qt
from PySide2.QtGui import QDoubleValidator, QPainter
from PySide2.QtPrintSupport import QPrintDialog, QPrinter
from PySide2.QtWebEngineWidgets import QWebEngineSettings
from model import Model
from shutil import copy2
from ds_exception import NotEnoughMoney
from report import AccountReport
from tempfile import TemporaryDirectory
from PIL.ImageQt import ImageQt
from pdf2image import convert_from_path
from view import View
from threading import Thread


class Control:
    def __init__(self):
        self.view = View()
        self.model = Model()
        self.only_double = QDoubleValidator()
        self.today = QDate.currentDate()
        self.source_table = None
        self.last_reverse_entry_btn = None  # for uncheck reversed entry button group
        self.settings = QWebEngineSettings.globalSettings()
        Thread(target=self.fil_upto_today, daemon=True).start()
        self.set_events()
        self.set_method_of_trans()

    def set_events(self):
        self.view.date_of_entry.setDate(self.today)
        self.view.report_date_from.setDate(self.today)
        self.view.report_date_to.setDate(self.today)
        self.view.trans_type.currentTextChanged.connect(self.set_method_of_trans)
        self.view.method_of_trans.currentTextChanged.connect(self.more_trans_complete)
        self.view.clear_entry_button.pressed.connect(self.clear_entries)
        self.view.actionAbut_DS_Manager.triggered.connect(View.show_about_ds)
        self.view.money.setValidator(self.only_double)
        self.view.enter_data_button.pressed.connect(self.enter_data)
        self.view.actionBackup_Database.triggered.connect(self.take_backup)
        self.view.preview_report_button.pressed.connect(self.preview_report)
        self.view.export_pdf_button.pressed.connect(self.save_pdf)
        self.view.reversed_entry_btn_group.buttonClicked.connect(self.set_reverse_entry)
        self.view.source_btn_group.buttonClicked.connect(self.set_source_table)
        self.view.print_report_button.pressed.connect(self.print_report)
        self.settings.setAttribute(
            QWebEngineSettings.LocalContentCanAccessFileUrls, True
        )
        self.settings.setAttribute(
            QWebEngineSettings.LocalContentCanAccessRemoteUrls, True
        )
        self.settings.setAttribute(QWebEngineSettings.LocalStorageEnabled, True)
        self.settings.setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        self.view.actionRestore_Database.triggered.connect(self.restore_db)

    def show(self):
        self.view.show()

    def fil_upto_today(self):
        for table in ["BANK", "CASH", "BUILDING"]:
            Model.fill_upto_today_balance(table)

    def set_method_of_trans(self):
        if self.view.trans_type.currentIndex() <= 1:
            self.view.method_of_trans.show()
            self.view.label_3.show()
            self.view.label_9.show()
            self.view.more_trans_detail.show()
            self.view.cash_radio.show()

        if self.view.trans_type.currentIndex() == 0:
            self.view.method_of_trans.clear()
            self.view.method_of_trans.insertItems(
                0,
                [
                    "Shantha Money",
                    "Till Box",
                    "Rent",
                    "Jumma Collection",
                    "Building Fund Collection",
                    "Others",
                ],
            )
        elif self.view.trans_type.currentIndex() == 1:
            self.view.method_of_trans.clear()
            self.view.method_of_trans.insertItems(
                0,
                [
                    "Salary",
                    "Electricity Bill",
                    "Water Bill",
                    "Refreshment",
                    "Jumma Expenses",
                    "Building Expenses",
                    "Maintenance",
                    "Others",
                ],
            )

        else:
            self.view.method_of_trans.hide()
            self.view.label_3.hide()
            self.view.label_9.hide()
            self.view.more_trans_detail.hide()
            self.view.cash_radio.hide()
            self.view.cheque_number.hide()
            self.view.cheque_label.hide()

    def more_trans_complete(self):
        curr_text = self.view.method_of_trans.currentText()
        helping = []
        if curr_text == "Salary":
            for value in (
                "Bash Imam",
                "Ass. Imam",
                "Muazzin",
                "Ass. Muazzin",
                "Sibithi",
                "Akshah",
                "Sadarth",
            ):
                helping.append(value)
        elif curr_text == "Till Box":
            for value in ("1", "2"):
                helping.append(value)
        elif curr_text == "Maintenance":
            for value in ("Labourer charge", "Material charge", "Cleaning"):
                helping.append(value)

        completer = QCompleter(helping)
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.view.more_trans_detail.setCompleter(completer)

    def clear_entries(self):
        self.view.trans_type.setCurrentIndex(0)
        self.view.more_trans_detail.clear()
        self.view.cheque_number.clear()
        self.view.money.clear()
        self.view.date_of_entry.setDate(self.today)
        self.view.cheque_label.hide()
        self.view.cheque_number.hide()
        self.view.cheque_number.clear()
        self.view.source_btn_group.setExclusive(False)
        self.view.reversed_entry_btn_group.setExclusive(False)
        self.last_reverse_entry_btn = None
        self.source_table = None
        try:
            self.view.source_btn_group.checkedButton().setChecked(False)
        except AttributeError:
            pass
        try:
            self.view.reversed_entry_btn_group.checkedButton().setChecked(False)
        except AttributeError:
            pass
        self.view.reversed_entry_btn_group.setExclusive(True)
        self.view.source_btn_group.setExclusive(True)

    def enter_data(self):
        if not self.verify_inputs():
            return
        try:
            if self.view.trans_type.currentIndex() <= 1:

                self.model.data_entry(
                    self.view.trans_type.currentText(),
                    self.view.method_of_trans.currentText(),
                    self.view.more_trans_detail.text(),
                    self.view.date_of_entry.date().toPython(),
                    self.source_table,
                    self.view.cheque_number.text(),
                    float(self.view.money.text()),
                )

            else:
                self.model.bank_update(
                    self.view.trans_type.currentText(),
                    self.view.date_of_entry.date().toPython(),
                    float(self.view.money.text()),
                    self.source_table,
                )

            View.show_message("Data Inserted Succesfully", "info")
        except NotEnoughMoney as e:
            View.show_message(e.message, "error")

    def take_backup(self):
        file, _ = QFileDialog.getSaveFileName(
            self.view,
            "Select DB Backup Folder",
            f"accounts_backup_{self.today.toPython()}",
            "Database (*.db)",
        )
        if file != "":
            copy2("account.db", file)
            View.show_message("Succesfully Backuped Database", "info")

    def verify_inputs(self):
        if (
            self.view.date_of_entry.date().toJulianDay()
            > QDate.currentDate().toJulianDay()
        ):
            View.show_message("Selected date should not exceed today date", "error")
            return False
        if self.view.trans_type.currentIndex() <= 1:
            if self.view.money.text() != "":
                if self.source_table == "CASH":
                    return True
                elif self.view.source_btn_group.checkedId() > 1:
                    if self.view.cheque_number.text() != "":
                        return True
                    View.show_message("Enter Cheque Number", "error")
                else:
                    View.show_message("Select money Source", "error")
            else:
                View.show_message("Please Enter money", "error")
        else:
            if self.source_table is not None:
                if self.view.money.text() != "":
                    return True
                else:
                    View.show_message("Please Enter money", "error")
            else:
                View.show_message("Select money Source", "error")
        return False

    def preview_report(self):
        if not self.validate_report_dates():
            return

        entries = self.model.get_records(
            self.view.report_date_from.date().toPython(),
            self.view.report_date_to.date().toPython(),
            self.view.comboBox.currentText(),
        )
        balance = self.model.get_balance(
            self.view.report_date_from.date().toPython(),
            self.view.report_date_to.date().toPython(),
        )
        if self.create_pdf(self.model.pdf_file.name, entries, balance):
            self.view.view_pdf(self.model.pdf_js, self.model.pdf_file.name)

    def create_pdf(self, pdf_file, entries, balance):
        try:
            AccountReport(
                pdf_file,
                entries,
                balance,
                self.view.report_date_from.date().toPython(),
                self.view.report_date_to.date().toPython(),
                self.view.comboBox.currentText(),
            )
            return True
        except TypeError:
            View.show_message(
                "Invalid Dates\nNo Entries Available within the period", "error"
            )
            return False

    def save_pdf(self):
        if self.validate_report_dates():
            file, _ = QFileDialog.getSaveFileName(
                self.view,
                "Select PDF Save Folder",
                f"report_{self.view.report_date_from.date().toPython()}_from_{self.view.report_date_to.date().toPython()}",
                "PDF (*.pdf)",
            )
            if file != "":
                file = file if file.endswith(".pdf") else file + ".pdf"
                entries = self.model.get_records(
                    self.view.report_date_from.date().toPython(),
                    self.view.report_date_to.date().toPython(),
                    self.view.comboBox.currentText(),
                )
                balance = self.model.get_balance(
                    self.view.report_date_from.date().toPython(),
                    self.view.report_date_to.date().toPython(),
                )
                self.create_pdf(file, entries, balance)

    def set_reverse_entry(self, checkbox):
        if self.last_reverse_entry_btn == checkbox.text():
            self.view.reversed_entry_btn_group.setExclusive(False)
            checkbox.setChecked(False)
            self.view.reversed_entry_btn_group.setExclusive(True)
            self.last_reverse_entry_btn = None
            self.view.more_trans_detail.clear()
            if "-" in self.view.money.text():
                self.view.money.setText(str(self.view.money.text()).lstrip("-"))
            return

        self.last_reverse_entry_btn = checkbox.text()

        if checkbox.text() == "Decrease":
            if not "-" in self.view.money.text():
                self.view.money.setText(f"-{self.view.money.text()}")
            self.view.more_trans_detail.setText("Reverse Entry")
        elif checkbox.text() == "Increase":
            self.view.more_trans_detail.setText("Reverse Entry")
            if "-" in self.view.money.text():
                self.view.money.setText(str(self.view.money.text()).lstrip("-"))

    def validate_report_dates(self):
        if (
            self.view.report_date_from.date().toJulianDay()
            or self.view.report_date_to.date().toJulianDay()
        ) > self.today.toJulianDay():
            View.show_message("Selected date should not exceed today date", "error")
            return False
        if (
            self.view.report_date_to.date().toJulianDay()
            - self.view.report_date_from.date().toJulianDay()
            < 0
        ):
            View.show_message("Deference between dates shoud be positive", "error")
            return False
        return True

    def print_report(self):
        if not self.validate_report_dates():
            return

        entries = self.model.get_records(
            self.view.report_date_from.date().toPython(),
            self.view.report_date_to.date().toPython(),
            self.view.comboBox.currentText(),
        )
        balance = self.model.get_balance(
            self.view.report_date_from.date().toPython(),
            self.view.report_date_to.date().toPython(),
        )
        if not self.create_pdf(self.model.pdf_file.name, entries, balance):
            return

        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer)
        if dialog.exec_() != QPrintDialog.Accepted:
            return

        with TemporaryDirectory() as path:
            images = convert_from_path(
                self.model.pdf_file.name, dpi=300, output_folder=path
            )
            painter = QPainter()
            painter.begin(printer)
            for i, image in enumerate(images):
                if i > 0:
                    printer.newPage()
                rect = painter.viewport()
                qtImage = ImageQt(image)
                qtImageScaled = qtImage.scaled(
                    rect.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
                )
                painter.drawImage(rect, qtImageScaled)
            painter.end()

    def set_source_table(self, radio_button):
        if radio_button.text() == "Cash":
            self.source_table = "CASH"
            self.view.cheque_number.clear()
            self.view.cheque_number.hide()
            self.view.cheque_label.hide()
            return
        elif radio_button.text() == "Main Account":
            self.source_table = "BANK"
        elif radio_button.text() == "Building Account":
            self.source_table = "BUILDING"
        if self.view.trans_type.currentIndex() < 2:
            self.view.cheque_label.show()
            self.view.cheque_number.show()

    def restore_db(self):
        file, _ = QFileDialog.getOpenFileName(
            self.view, "Select Database File", "", "Database (*.db)",
        )
        if file != "":
            copy2(file, "account.db")
            View.show_message("Succesfully Restored Database", "info")
