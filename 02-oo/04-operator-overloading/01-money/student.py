class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        if self.currency == other.currency:
            return Money(
                self.amount + other.amount,
                self.currency
            )
        else:
            raise RuntimeError("Mismatched currencies!")

    def __sub__(self, other):
        if self.currency == other.currency:
            return Money(
                self.amount - other.amount,
                self.currency
            )
        else:
            raise RuntimeError("Mismatched currencies!")

    def __mul__(self, other):
        if self.currency == other.currency:
            return Money(
                self.amount * other.amount,
                self.currency
            )
        else:
            raise RuntimeError("Mismatched currencies!")

    def __mul__(self, num):
        if isinstance(num, int) or isinstance(num, float):
            return Money(
                self.amount * num,
                self.currency
            )
        else:
            raise RuntimeError(f"{num} is not a number!")
