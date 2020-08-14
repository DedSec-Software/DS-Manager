from sqlite3 import connect
from datetime import date as datetime
from ds_exception import NotEnoughMoney


class Model:
    def __init__(self):
        self.conn = connect("account.db")
        self.cur = self.conn.cursor()

    def data_entry(
        self, trans_type, method_of_trans, description, date, money_type, amount: float
    ):
        self.cur.execute(
            f"INSERT INTO {'INCOME' if trans_type == 'Income' else 'EXPENSE'} VALUES (:name,:desc, :date, :money_type, :amount)",
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

        balance, last_date, count = self.get_source_last_update(source_table)
        if last_date == date:
            self.source_update_entry(source_table, trans_type, count, amount)
        else:
            self.source_insert_entry(
                source_table, trans_type, count, date, balance, amount
            )

    def source_update_entry(self, source_table, trans_type, count, amount):
        self.cur.execute(
            f"UPDATE {source_table} SET balance=balance {'+' if trans_type == 'Income' else '-'} :amount WHERE id={count}",
            {"amount": amount},
        )
        return self.conn.commit()

    def source_insert_entry(
        self, source_table, trans_type, count, date, balance, amount
    ):
        self.cur.execute(
            f"INSERT INTO {source_table} VALUES (:id, :date, :balance {'+' if trans_type == 'Income' else '-'} :amount)",
            {"id": count + 1, "date": date, "balance": balance, "amount": amount,},
        )
        return self.conn.commit()

    def get_source_last_update(self, source_table):
        self.cur.execute(f"SELECT COUNT(*) FROM {source_table}")
        count = self.cur.fetchone()[0]
        self.cur.execute(f"SELECT balance FROM {source_table} WHERE id={count};")
        balance = self.cur.fetchone()[0]
        self.cur.execute(f"SELECT date FROM {source_table} WHERE id={count};")
        last_date = self.cur.fetchone()[0]
        return (balance, last_date, count)

    def bank_update(self, trans_type, date, amount: float):
        bank_balance, bank_last_date, count_bank = self.get_source_last_update("BANK")
        cash_balance, cash_last_date, count_cash = self.get_source_last_update("CASH")
        if trans_type == "Bank Deposit":
            if cash_balance >= amount:
                if bank_last_date == date:
                    self.cur.execute(
                        f"UPDATE BANK SET balance=balance + :amount WHERE id={count_bank}",
                        {"amount": amount},
                    )
                    self.conn.commit()

                else:
                    self.cur.execute(
                        "INSERT INTO BANK VALUES (:id, :date, :amount)",
                        {
                            "id": count_bank + 1,
                            "date": date,
                            "amount": bank_balance + amount,
                        },
                    )
                    self.conn.commit()

                if cash_last_date == date:
                    self.cur.execute(
                        f"UPDATE CASH SET balance=balance - :amount WHERE id={count_cash}",
                        {"amount": amount},
                    )
                    self.conn.commit()

                else:
                    self.cur.execute(
                        "INSERT INTO CASH VALUES (:id, :date, :amount)",
                        {
                            "id": count_cash + 1,
                            "date": date,
                            "amount": cash_balance - amount,
                        },
                    )
                    self.conn.commit()
            else:
                raise NotEnoughMoney("Not Enough money in cash balance")

        elif trans_type == "Bank Withdraw":
            if bank_balance >= amount:
                if bank_last_date == date:
                    self.cur.execute(
                        f"UPDATE BANK SET balance=balance - :amount WHERE id={count_bank}",
                        {"amount": amount},
                    )
                    self.conn.commit()

                else:
                    self.cur.execute(
                        "INSERT INTO BANK VALUES (:id, :date, :amount)",
                        {
                            "id": (count_bank + 1),
                            "date": date,
                            "amount": (bank_balance - amount),
                        },
                    )
                    self.conn.commit()

                if cash_last_date == date:
                    self.cur.execute(
                        f"UPDATE CASH SET balance=balance + :amount WHERE id={count_cash}",
                        {"amount": amount},
                    )
                    self.conn.commit()

                else:
                    self.cur.execute(
                        "INSERT INTO CASH VALUES (:id, :date, :amount)",
                        {
                            "id": count_cash + 1,
                            "date": date,
                            "amount": cash_balance + amount,
                        },
                    )
                    self.conn.commit()
            else:
                raise NotEnoughMoney("Not Enough money in main bank account")

    def get_records(self, date1, date2):
        self.cur.execute(
            "SELECT method_of_trans, description, date(date), money_type, amount from INCOME WHERE date BETWEEN :startdate AND :enddate ORDER BY date",
            {"startdate": date1, "enddate": date2},
        )
        rec_income = self.cur.fetchall()

        self.cur.execute(
            "SELECT method_of_trans, description, date(date), money_type, amount from EXPENSE WHERE date BETWEEN :startdate AND :enddate ORDER BY date",
            {"startdate": date1, "enddate": date2},
        )
        rec_expense = self.cur.fetchall()

        return (rec_income, rec_expense)

    def get_balance(self, date1, date2):
        self.cur.execute(
            "SELECT date(date), balance FROM BANK WHERE date BETWEEN :startdate AND :enddate ORDER BY id DESC LIMIT 1",
            {"startdate": date1, "enddate": date2},
        )
        final_bank_balance = self.cur.fetchone()

        self.cur.execute(
            "SELECT date(date), balance FROM CASH WHERE date BETWEEN :startdate AND :enddate ORDER BY id DESC LIMIT 1",
            {"startdate": date1, "enddate": date2},
        )
        final_cash_balance = self.cur.fetchone()

        self.cur.execute(
            "SELECT date(date), balance FROM BUILDING WHERE date BETWEEN :startdate AND :enddate ORDER BY id DESC LIMIT 1",
            {"startdate": date1, "enddate": date2},
        )
        final_building_balance = self.cur.fetchone()

        return (final_bank_balance, final_cash_balance, final_building_balance)

    def close_connection(self):
        return self.conn.close()
