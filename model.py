from sqlite3 import connect
from datetime import date as datetime
from ds_exception import NotEnoughMoney


class Model:
    def __init__(self):
        self.conn = connect("account.db")
        self.cur = self.conn.cursor()

    def data_entry(self, trans_type, method_of_trans, description, date, money_type, amount: float):
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
        bank_balance, bank_last_date, count_bank = self.get_bank_last_update()
        cash_balance, cash_last_date, count_cash = self.get_cash_last_update()
        if money_type == "Bank":
            if bank_last_date == date:
                self.cur.execute(
                    f"UPDATE BANK SET balance=balance {'+' if trans_type == 'Income' else '-'} :amount WHERE id={count_bank}",
                    {"amount": amount},
                )
                self.conn.commit()

            else:
                self.cur.execute(
                    f"INSERT INTO BANK VALUES (:id, :date, :balance {'+' if trans_type == 'Income' else '-'} :amount)",
                    {
                        "id": count_bank + 1,
                        "date": date,
                        "balance": bank_balance,
                        "amount": amount,
                    },
                )
                self.conn.commit()
        else:
            if cash_last_date == date:
                self.cur.execute(
                    f"UPDATE CASH SET balance=balance {'+' if trans_type == 'Income' else '-'} :amount WHERE id={count_cash}",
                    {"amount": amount},
                )
                self.conn.commit()

            else:
                self.cur.execute(
                    f"INSERT INTO CASH VALUES (:id, :date, :balance {'+' if trans_type == 'Income' else '-'} :amount)",
                    {
                        "id": count_cash + 1,
                        "date": date,
                        "balance": cash_balance,
                        "amount": amount,
                    },
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


    def get_records(self, date1, date2):
        self.cur.execute(
            f"SELECT * from INCOME WHERE date BETWEEN :startdate AND :enddate ORDER BY date",
            {
                "startdate" = date1,
                "enddate" = date2
            }
        )
        rec_income = self.cur.fetchall()

        self.cur.execute(
            f"SELECT * from EXPENSE WHERE date BETWEEN :startdate AND :enddate ORDER BY date",
            {
                "startdate" = date1,
                "enddate" = date2
            }
        )
        rec_expense = self.cur.fetchall()

        return(rec_income, rec_expense)

    def get_balance(self, date1, date2):
        self.cur.execute(
            f"SELECT * FROM BANK WHERE date BETWEEN :startdate AND :enddate ORDER BY id DESC LIMIT 1",
            {
                "startdate" = date1,
                "enddate" = date2
            }
        )
        final_bank_balance = self.cur.fetchall()

        self.cur.execute(
            f"SELECT * FROM CASH WHERE date BETWEEN :startdate AND :enddate ORDER BY id DESC LIMIT 1",
            {
                "startdate" = date1,
                "enddate" = date2
            }
        )
        final_cash_balance = self.cur.fetchall()


        return(final_bank_balance, final_cash_balance)



    def close_connection(self):
        return self.conn.close()
