class DifferentCurrencyError(Exception):
    pass


class Currency:
    """
    Represents a currency. Does not contain any exchange rate info.
    """

    def __init__(self, name, code, symbol=None, digits=2):
        self.name = name
        self.code = code
        self.symbol = symbol
        self.digits = digits
        """
        Parameters:
        - name -- the English name of the currency
        - code -- the ISO 4217 three-letter code for the currency
        - symbol - optional symbol used to designate currency
        - digits -- number of significant digits used
        """  
        # dollar = Currency("United States dollar", "USD", "$")
        # peso = Currency("Mexican peso", "MXD")
        # dinar = Currency("Bahraini dinar", "BHD", digits=3)
        

    def __str__(self):
        """
        Should return the currency code, or code with symbol in parentheses.
        """
        pass

    def __eq__(self, other):
        """
        All fields must be equal to for the objects to be equal.
        """
        return (type(self) == type(other) and self.name == other.name and
                self.code == other.code and self.symbol == other.symbol and
                self.digits == other.digits)


class Money:
    """
    Represents an amount of money. Requires an amount and a currency.
    """
  

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
        """
        Parameters:
        - amount -- quantity of currency
        - currency -- type of currency
        """
    

    def __str__(self):
        """
        Should use the currency symbol if available, else use the code.
        Use the currency digits to determine number of digits to show.
        """
        if self.currency.symbol is not None:
            return f"{self.currency.symbol}{self.amount:.{self.currency.digits}f}"
        else:
            return f"{self.currency.code} {self.amount:.{self.currency.digits}f}"

    def __repr__(self):
        return f"<Money {str(self)}>"

    def __eq__(self, other):
        """
        All fields must be equal to for the objects to be equal.
        """
        return (type(self) == type(other) and self.amount == other.amount and
                self.currency == other.currency)

    def add(self, other):

        """
        Add two money objects of the same currency. If they have different
        currencies, raise a DifferentCurrencyError.
        """

        # self.(amount, currency) = amount
        # self.other = other
        # if not (isinstance(self, int) and isinstance(other, int)):
            # raise DifferentCurrencyError(Exception)
        new_amount = self.amount + other.amount
        if (self.currency == other.currency):
            return Money(new_amount, self.currency)
        else:
            raise DifferentCurrencyError

        # pass


    def sub(self, other):
        """
        Subtract two money objects of the same currency. If they have different
        currencies, raise a DifferentCurrencyError.
        """

        new_amount = self.amount - other.amount
        if (self.currency == other.currency):
            return Money(new_amount, self.currency)
        else:
            raise DifferentCurrencyError
        
        pass

    def mul(self, multiplier):
        """
        Multiply a money object by a number to get a new money object.
        """
        new_amount = self.amount * multiplier
        return Money(new_amount, self.currency)

        pass

    def div(self, divisor):
        """
        Divide a money object by a number to get a new money object.
        """

        new_amount = self.amount / divisor
        return Money(new_amount, self.currency)

        pass
