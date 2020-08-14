#  Copyright (c) 2020. Mohamed Zumair <mhdzumair@gmail.com>
from PySide2.QtWidgets import QMainWindow, QCompleter, QDialog, QFileDialog
from PySide2.QtCore import QDate, Qt
from PySide2.QtGui import QDoubleValidator
from dsmanager import Ui_DedSecWindow
from about import Ui_Dialog
from model import Model
from shutil import copy2
from ds_exception import NotEnoughMoney
from report import AccountReport
from pdfviewer import Ui_MainWindow
from tempfile import NamedTemporaryFile
from os import unlink


class Control(QMainWindow, Ui_DedSecWindow):
    def __init__(self, *args, **kwargs):
        super(Control, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.date_of_entry.setDate(QDate.currentDate())
        self.report_date_from.setDate(QDate.currentDate())
        self.report_date_to.setDate(QDate.currentDate())
        self.trans_type.currentTextChanged.connect(self.set_method)
        self.method_of_trans.currentTextChanged.connect(self.more_trans_complete)
        self.clear_entry_button.pressed.connect(self.clear_entries)
        self.actionAbut_DS_Manager.triggered.connect(self.show_about_ds)
        self.only_double = QDoubleValidator()
        self.money.setValidator(self.only_double)
        self.set_method()
        self.model = Model()
        self.enter_data_button.pressed.connect(self.enter_data)
        self.actionBackup_Database.triggered.connect(self.take_backup)
        self.preview_report_button.pressed.connect(self.preview_report)
        self.pdf_file = NamedTemporaryFile(suffix=".pdf", delete=False)
        self.export_pdf_button.pressed.connect(self.save_pdf)

    def closeEvent(self, event):
        self.model.close_connection()
        self.pdf_file.close()
        unlink(self.pdf_file.name)
        event.accept()

    def set_method(self):
        if self.trans_type.currentText() == "Income" or "Expense":
            self.method_of_trans.show()
            self.label_3.show()
            self.label_9.show()
            self.more_trans_detail.show()
            self.label_10.show()
            self.radioButton.show()
            self.radioButton_2.show()

        if self.trans_type.currentText() == "Income":
            self.method_of_trans.clear()
            self.method_of_trans.insertItems(
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
        elif self.trans_type.currentText() == "Expense":
            self.method_of_trans.clear()
            self.method_of_trans.insertItems(
                0,
                [
                    "Salary",
                    "Electricity Bill",
                    "Water Bill",
                    "Refreshment",
                    "Jumma Expenses",
                    "Building Expenses",
                    "Maintenance",
                ],
            )
        else:
            self.method_of_trans.hide()
            self.label_3.hide()
            self.label_9.hide()
            self.more_trans_detail.hide()
            self.label_10.hide()
            self.radioButton.hide()
            self.radioButton_2.hide()

    def more_trans_complete(self):
        curr_text = self.method_of_trans.currentText()
        if curr_text == "Building Expenses" or curr_text == "Building Fund Collection":
            self.label_10.hide()
            self.radioButton.hide()
            self.radioButton_2.hide()
        else:
            self.label_10.show()
            self.radioButton.show()
            self.radioButton_2.show()

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
        self.more_trans_detail.setCompleter(completer)

    def clear_entries(self):
        self.trans_type.setCurrentIndex(0)
        self.more_trans_detail.clear()
        self.money.clear()
        self.date_of_entry.setDate(QDate.currentDate())

    def show_about_ds(self):
        dialog = QDialog()
        about = Ui_Dialog()
        about.setupUi(dialog)
        dialog.exec_()

    def enter_data(self):
        if self.verify_inputs():
            if self.trans_type.currentIndex() <= 1:

                if self.method_of_trans.currentText().startswith("Building"):
                    source = "Building"
                elif self.radioButton.isChecked():
                    source = "Bank"
                else:
                    source = "Cash"

                self.model.data_entry(
                    self.trans_type.currentText(),
                    self.method_of_trans.currentText(),
                    self.more_trans_detail.text(),
                    self.date_of_entry.date().toJulianDay(),
                    source,
                    float(self.money.text()),
                )
                self.show_message("Data Inserted Succesfully", "info")

            else:
                try:
                    self.model.bank_update(
                        self.trans_type.currentText(),
                        self.date_of_entry.date().toJulianDay(),
                        float(self.money.text()),
                    )
                    self.show_message("Data Inserted Succesfully", "info")
                except NotEnoughMoney as e:
                    self.show_message(e.message, "error")

    def take_backup(self):
        file = QFileDialog.getSaveFileName(
            self,
            "Select DB Backup Folder",
            f"accounts_backup_{QDate.currentDate().toPython()}",
            "Database (*.db)",
        )
        if file:
            try:
                copy2("account.db", file[0])
            except FileNotFoundError:
                pass

    def verify_inputs(self):
        if self.trans_type.currentIndex() <= 1:
            if (
                self.radioButton.isChecked()
                or self.radioButton_2.isChecked()
                or self.method_of_trans.currentText().startswith("Building")
            ):
                if self.money.text() != "":
                    return True
                else:
                    self.show_message("Please Enter money", "error")
            else:
                self.show_message("select money Source", "error")
        else:
            if self.money.text() != "":
                return True
            else:
                self.show_message("Please Enter money", "error")
        return False

    def preview_report(self):
        entries = self.model.get_records(
            self.report_date_from.date().toJulianDay(),
            self.report_date_to.date().toJulianDay(),
        )
        balance = self.model.get_balance(
            self.report_date_from.date().toJulianDay(),
            self.report_date_to.date().toJulianDay(),
        )
        self.create_pdf(self.pdf_file.name, entries, balance)
        main_window = QMainWindow(self)
        main_window.setWindowTitle("Ds Manager - Pdf viewer")
        pdfviewer = Ui_MainWindow()
        pdfviewer.setupUi(main_window)
        pdfviewer.set_pdf(self.pdf_file.name)
        pdfviewer.show_pdf(main_window)

    def create_pdf(self, pdf_file, entries, balance):
        return AccountReport(
            pdf_file,
            entries,
            balance,
            self.report_date_from.date().toPython(),
            self.report_date_to.date().toPython(),
            self.comboBox.currentText(),
        )

    def save_pdf(self):
        file = QFileDialog.getSaveFileName(
            self,
            "Select PDF Save Folder",
            f"report_{self.report_date_from.date().toPython()}_from_{self.report_date_to.date().toPython()}",
            "PDF (*.pdf)",
        )
        entries = self.model.get_records(
            self.report_date_from.date().toJulianDay(),
            self.report_date_to.date().toJulianDay(),
        )
        balance = self.model.get_balance(
            self.report_date_from.date().toJulianDay(),
            self.report_date_to.date().toJulianDay(),
        )
        if file[0] != "":
            self.create_pdf(file[0], entries, balance)
