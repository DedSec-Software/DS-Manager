from sqlite3 import connect


class Model:
    def __init__(self):
        self.conn = connect("account.db")
        self.cur = self.conn.cursor()

    def data_entry(self, trans_type, method_of_trans, description, date, money_type, amount):
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

    def update_entry(self, trans_type, money_type, date, amount):
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

    def bank_update(self, trans_type, date, amount):

        #Fetching Data from Tables Start

        self.cur.execute("SELECT COUNT(*) FROM BANK")
        count_bank = self.cur.fetchone()[0]

        self.cur.execute("SELECT COUNT(*) FROM CASH;")
        count_cash = self.cur.fetchone()[0]

        self.cur.execute("SELECT balance FROM BANK WHERE id='count_bank';")
        balance_bank = self.cur.fetchone()[0]

        self.cur.execute("SELECT balance FROM CASH WHERE id='count_cash'")
        balance_cash = self.cur.fetchone()[0]

        self.cur.execute("SELECT date FROM BANK WHERE id='count_bank';")
        date_bank = self.cur.fetchone()[0]

        self.cur.execute("SELECT date FROM CASH WHERE id='count_cash'")
        date_cash = self.cur.fetchone()[0]

        #Fetching Data from Tables End

        if trans_type == "Bank Deposit":
            if cash_balance >= amount:
                if date_bank == date:
                    self.cur.execute(
                        f"UPDATE BANK SET balance=balance + :amount WHERE id='{count_bank}'",
                        {"date": date, "amount": amount},
                    )
                    self.conn.commit()

                else:
                    self.cur.execute(
                        "INSERT INTO BANK VALUES (:id, :date; :amount)",
                        {"id"=count_bank+1, "date": date, "amount": balance_bank + amount},
                    )
                    self.conn.commit()

                if date_cash == date:
                    self.cur.execute(
                    f"UPDATE CASH SET balance=balance - :amount WHERE id='{count_cash}'",
                    {"date": date, "amount": amount},
                    )
                    self.conn.commit()

                else:
                    self.cur.execute(
                    "INSERT INTO CASH VALUES (:id, :date; :amount)",
                    {"id"=count_cash+1, "date": date, "amount": cash_balance - amount},
                    )
                    self.conn.commit()
            else:
                Raise error message here
                For Your Work :D

        elif trans_type == "Bank Withdraw":
            if balance_bank >= amount:
                if date_bank == date:
                    self.cur.execute(
                        f"UPDATE BANK SET balance=balance - :amount WHERE id='{count_bank}'",
                        {"date": date, "amount": amount},
                    )
                    self.conn.commit()

                else:
                    self.cur.execute(
                        "INSERT INTO BANK VALUES (:id, :date; :amount)",
                        {"id"=count_bank+1, "date": date, "amount": balance_bank - amount},
                    )
                    self.conn.commit()

                if date_cash == date:
                    self.cur.execute(
                    f"UPDATE CASH SET balance=balance + :amount WHERE id='{count_cash}'",
                    {"date": date, "amount": amount},
                    )
                    self.conn.commit()

                else:
                    self.cur.execute(
                    "INSERT INTO CASH VALUES (:id, :date; :amount)",
                    {"id"=count_cash+1, "date": date, "amount": cash_balance + amount}
                    )
                    self.conn.commit()
            else:
                Raise error message here
                For Your Work :D

    def close_connection(self):
        return self.conn.close()
