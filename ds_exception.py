#  Copyright (c) 2020 - 2021. Mohamed Zumair <mhdzumair@gmail.com


class NotEnoughMoney(Exception):
    """
    raise error when note Enough money in respective accounts.

    Args:
        message (str): Exception message;

    Returns:
        None;

    Raises:
        Exception: NotEnoughMoney

    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
