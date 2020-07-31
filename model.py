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

    def update_entry(self, trans_type, money_type, date, amount: float):
        if money_type == "Bank":
            self.cur.execute(
                f"UPDATE BANK SET balance=balance {'+' if trans_type == 'Income' else '-'} :amount, date = :date WHERE id='1'",
                {"date": date, "amount": amount},
            )

        elif money_type == "Cash":
            self.cur.execute(
                f"UPDATE CASH SET balance=balance {'+' if trans_type == 'Income' else '-'} :amount, date= :date WHERE id='1'",
                {"date": date, "amount": amount},
            )

        self.conn.commit()

    def get_bank_last_update(self):
        self.cur.execute("SELECT COUNT(*) FROM BANK")
        count_bank = self.cur.fetchone()[0]
        self.cur.execute(f"SELECT balance FROM BANK WHERE id={count_bank};")
        bank_balance = self.cur.fetchone()[0]
        self.cur.execute(f"SELECT date FROM BANK WHERE id={count_bank};")
        bank_last_date = self.cur.fetchone()[0]
        return (bank_balance, bank_last_date, count_bank)

    def get_cash_last_update(self):
        self.cur.execute("SELECT COUNT(*) FROM CASH;")
        count_cash = self.cur.fetchone()[0]
        self.cur.execute(f"SELECT balance FROM CASH WHERE id={count_cash};")
        cash_balance = self.cur.fetchone()[0]
        self.cur.execute(f"SELECT date FROM CASH WHERE id={count_cash};")
        cash_last_date = self.cur.fetchone()[0]
        return (cash_balance, cash_last_date, count_cash)

    def bank_update(self, trans_type, date, amount: float):
        bank_balance, bank_last_date, count_bank = self.get_bank_last_update()
        cash_balance, cash_last_date, count_cash = self.get_cash_last_update()
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

    def close_connection(self):
        return self.conn.close()
