#  Copyright (C) 2020 - 2021  Pakeetharan Balasupramaniyam <pakee@gmail.com>
#  Copyright (C) 2020 - 2021 Mohamed Zumair <mhdzumair@gmail.com>
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

from os import unlink
from os.path import abspath
from sqlite3 import connect
import datetime
from tempfile import NamedTemporaryFile

from ds_exception import NotEnoughMoney


def singleton(class_):
    class SingletonClass(class_):
        _instance = None

        def __new__(cls, *args, **kwargs):
            if SingletonClass._instance is None:
                SingletonClass._instance = super(SingletonClass, cls).__new__(
                    cls, *args, **kwargs
                )
                SingletonClass._instance._sealed = False
            return SingletonClass._instance

        def __init__(self, *args, **kwargs):
            if self._sealed:
                return
            super(SingletonClass, self).__init__(*args, **kwargs)
            self._sealed = True

    SingletonClass.__name__ = class_.__name__
    return SingletonClass


@singleton
class Model:
    def __init__(self):
        self.connection = connect("account.db")
        self.cursor = self.connection.cursor()
        self.pdf_file = NamedTemporaryFile(suffix=".pdf", delete=False)
        self.pdf_js = abspath("inc/pdfjs/web/viewer.html")

    def data_entry(
        self,
        trans_type,
        method_of_trans,
        description,
        date,
        source_table,
        cheque_number,
        amount: float,
    ):
        print(
            trans_type,
            method_of_trans,
            description,
            date,
            source_table,
            cheque_number,
            amount,
        )
        self.cursor.execute(
            f"INSERT INTO {'INCOME' if trans_type == 'Income' else 'EXPENSE'} "
            " VALUES (:name,:desc, julianday(:date), :money_type, :cheque_number, :amount)",
            {
                "name": method_of_trans,
                "desc": description,
                "date": date,
                "money_type": source_table,
                "cheque_number": cheque_number,
                "amount": amount,
            },
        )
        self.connection.commit()

        if trans_type == "Income":
            symbol = "+"
        else:
            symbol = "-"
        self.source_update_entry(source_table, symbol, date, amount)

    def source_update_entry(self, source_table, symbol, date, amount):
        self.cursor.execute(
            f"UPDATE {source_table} SET balance=balance {symbol} :amount WHERE date >= julianday(:date);",
            {"amount": amount, "date": date},
        )
        return self.connection.commit()

    def bank_update(self, trans_type, date, amount: float, source_table):
        if trans_type == "Bank Deposit":
            self.source_update_entry(source_table, "+", date, amount)
            self.source_update_entry("CASH", "-", date, amount)

        elif trans_type == "Bank Withdraw":
            self.source_update_entry("CASH", "+", date, amount)
            self.source_update_entry(source_table, "-", date, amount)

        self.connection.commit()

    def get_records(self, start_date, end_date, level):
        if level == "1":
            self.cursor.execute(
                "SELECT method_of_trans, money_type, amount from INCOME WHERE "
                "date BETWEEN julianday(:startdate) AND julianday(:enddate) ORDER BY method_of_trans",
                {"startdate": start_date, "enddate": end_date},
            )
            income_entries = self.cursor.fetchall()

            self.cursor.execute(
                "SELECT method_of_trans, money_type, amount from EXPENSE WHERE "
                "date BETWEEN julianday(:startdate) AND julianday(:enddate) ORDER BY method_of_trans",
                {"startdate": start_date, "enddate": end_date},
            )
            expense_entries = self.cursor.fetchall()

            income_entries = sorting(income_entries)
            expense_entries = sorting(expense_entries)
        else:
            self.cursor.execute(
                "SELECT method_of_trans, description, date(date), money_type, cheque_number, amount "
                "from INCOME WHERE date BETWEEN julianday(:startdate) AND julianday(:enddate) ORDER BY date",
                {"startdate": start_date, "enddate": end_date},
            )
            income_entries = self.cursor.fetchall()

            self.cursor.execute(
                "SELECT method_of_trans, description, date(date), money_type, cheque_number, amount "
                "from EXPENSE WHERE date BETWEEN julianday(:startdate) AND julianday(:enddate) ORDER BY date",
                {"startdate": start_date, "enddate": end_date},
            )
            expense_entries = self.cursor.fetchall()

        return (income_entries, expense_entries)

    def get_balance(self, start_date, end_date):
        self.cursor.execute(
            "SELECT date(date), balance FROM BANK WHERE date BETWEEN "
            "julianday(:startdate) AND julianday(:enddate) ORDER BY date DESC LIMIT 1",
            {"startdate": start_date, "enddate": end_date},
        )
        final_bank_balance = self.cursor.fetchone()

        self.cursor.execute(
            "SELECT date(date), balance FROM CASH WHERE date BETWEEN "
            "julianday(:startdate) AND julianday(:enddate) ORDER BY date DESC LIMIT 1",
            {"startdate": start_date, "enddate": end_date},
        )
        final_cash_balance = self.cursor.fetchone()

        self.cursor.execute(
            "SELECT date(date), balance FROM BUILDING WHERE date BETWEEN "
            "julianday(:startdate) AND julianday(:enddate) ORDER BY date DESC LIMIT 1",
            {"startdate": start_date, "enddate": end_date},
        )
        final_building_balance = self.cursor.fetchone()

        return (final_bank_balance, final_cash_balance, final_building_balance)

    def close_connection(self):
        self.pdf_file.close()
        unlink(self.pdf_file.name)
        self.connection.close()

    @classmethod
    def fill_upto_today_balance(cls, source_table):
        connection = connect("account.db")
        cursor = connection.cursor()
        cursor.execute(f"SELECT date(MAX(date)), balance FROM {source_table}")
        last_entry_date, last_entry_money = cursor.fetchone()
        today = str(datetime.date.today())
        if last_entry_date == today:
            return

        start = datetime.datetime.strptime(last_entry_date, "%Y-%m-%d")
        end = datetime.datetime.strptime(today, "%Y-%m-%d")
        end += datetime.timedelta(1)
        start += datetime.timedelta(1)
        dates = [
            start + datetime.timedelta(days=x) for x in range(0, (end - start).days)
        ]
        for date in dates:
            date = date.strftime("%Y-%m-%d")
            cursor.execute(
                f"INSERT INTO {source_table} (date, balance) VALUES (julianday(:date), :balance)",
                {"date": date, "balance": last_entry_money},
            )
        connection.commit()


def sorting(entries):
    sorted_entries = []
    for entry in entries:
        index = None
        for row in sorted_entries:
            if entry[0] == row[0] and entry[1] == row[1]:
                index = sorted_entries.index(row)
                break

        if index is not None:
            sorted_entries[index][2] += entry[2]
        else:
            sorted_entries.append(list(entry))

    return sorted_entries
