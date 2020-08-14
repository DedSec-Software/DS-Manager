from sqlite3 import connect
import datetime
from ds_exception import NotEnoughMoney


class Model:
    def __init__(self):
        self.conn = connect("account.db")
        self.cur = self.conn.cursor()

    def data_entry(
        self, trans_type, method_of_trans, description, date, money_type, amount: float
    ):
        self.cur.execute(
            f"INSERT INTO {'INCOME' if trans_type == 'Income' else 'EXPENSE'} "
            " VALUES (:name,:desc, julianday(:date), :money_type, :amount)",
            {
                "name": method_of_trans,
                "desc": description,
                "date": date,
                "money_type": money_type,
                "amount": amount,
            },
        )
        self.conn.commit()

        if money_type == "Bank":
            source_table = "BANK"
        elif money_type == "Cash":
            source_table = "CASH"
        else:
            source_table = "BUILDING"

        if trans_type == "Income":
            symbol = "+"
        else:
            symbol = "-"
        self.source_update_entry(source_table, symbol, date, amount)

    def source_update_entry(self, source_table, symbol, date, amount):
        self.cur.execute(
            f"UPDATE {source_table} SET balance=balance {symbol} :amount WHERE date >= julianday(:date);",
            {"amount": amount, "date": date},
        )
        return self.conn.commit()

    def bank_update(self, trans_type, date, amount: float):
        if trans_type == "Bank Deposit":
            self.source_update_entry("BANK", "+", date, amount)
            self.source_update_entry("CASH", "-", date, amount)

        elif trans_type == "Bank Withdraw":
            self.source_update_entry("CASH", "+", date, amount)
            self.source_update_entry("BANK", "-", date, amount)

    def get_records(self, start_date, end_date, level):
        if level == "level 1":
            self.cur.execute(
                "SELECT method_of_trans, money_type, amount from INCOME WHERE "
                "date BETWEEN julianday(:startdate) AND julianday(:enddate) ORDER BY method_of_trans",
                {"startdate": start_date, "enddate": end_date},
            )
            income_entries = self.cur.fetchall()

            self.cur.execute(
                "SELECT method_of_trans, money_type, amount from EXPENSE WHERE "
                "date BETWEEN julianday(:startdate) AND julianday(:enddate) ORDER BY method_of_trans",
                {"startdate": start_date, "enddate": end_date},
            )
            expense_entries = self.cur.fetchall()
        else:
            self.cur.execute(
                "SELECT method_of_trans, description, date(date), money_type, amount "
                "from INCOME WHERE date BETWEEN julianday(:startdate) AND julianday(:enddate) ORDER BY date",
                {"startdate": start_date, "enddate": end_date},
            )
            income_entries = self.cur.fetchall()

            self.cur.execute(
                "SELECT method_of_trans, description, date(date), money_type, amount "
                "from EXPENSE WHERE date BETWEEN julianday(:startdate) AND julianday(:enddate) ORDER BY date",
                {"startdate": start_date, "enddate": end_date},
            )
            expense_entries = self.cur.fetchall()

        return (income_entries, expense_entries)

    def get_balance(self, start_date, end_date):
        self.cur.execute(
            "SELECT date(date), balance FROM BANK WHERE date BETWEEN "
            "julianday(:startdate) AND julianday(:enddate) ORDER BY date DESC LIMIT 1",
            {"startdate": start_date, "enddate": end_date},
        )
        final_bank_balance = self.cur.fetchone()

        self.cur.execute(
            "SELECT date(date), balance FROM CASH WHERE date BETWEEN "
            "julianday(:startdate) AND julianday(:enddate) ORDER BY date DESC LIMIT 1",
            {"startdate": start_date, "enddate": end_date},
        )
        final_cash_balance = self.cur.fetchone()

        self.cur.execute(
            "SELECT date(date), balance FROM BUILDING WHERE date BETWEEN "
            "julianday(:startdate) AND julianday(:enddate) ORDER BY date DESC LIMIT 1",
            {"startdate": start_date, "enddate": end_date},
        )
        final_building_balance = self.cur.fetchone()

        return (final_bank_balance, final_cash_balance, final_building_balance)

    def close_connection(self):
        return self.conn.close()

    def fill_upto_today_balance(self, source_table):
        self.cur.execute(f"SELECT date(MAX(date)), balance FROM {source_table}")
        last_entry_date, last_entry_money = self.cur.fetchone()
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
            self.cur.execute(
                f"INSERT INTO {source_table} (date, balance) VALUES (julianday(:date), :balance)",
                {"date": date, "balance": last_entry_money},
            )
        self.conn.commit()
