__author__ = 'maxiee'


class CreditCard:
    """ A consumer credit card
    """

    def __init__(self, customer, bank, acnt, limit, balance = 0):
        """
        Create a new credit card instance

        The initial balance is zero.

        :param customer: the name of the customer (e.g., 'Maxiee')
        :param bank: the name of the bank (e.g., 'Bank')
        :param acnt: the account identifier (e.g., '001 001')
        :param limit: credit limit (measured in RMB)
        :return:
        """

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price):
        """
        Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed; False if charge was denide.

        :param price:
        :return:
        """
        if not isinstance(price, (int, float)):
            raise TypeError('price must be numeric')
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """
        Process customer payment that reduces balance.

        :param amount:
        :return:
        """
        if not isinstance(amount, (int, float)):
            raise TypeError('amount must be numeric')
        if self._balance - amount < 0:
            raise ValueError('\n\tyou have %.3f, payment is %.3f,\n\tbalance will be negtive!!'
                             % (self._balance, amount))
        self._balance -= amount


if __name__ == '__main__':
    # test
    card_4 = CreditCard("c1", "bank1", "999", 5000)
    card_5 = CreditCard("c2", "bank2", "998", 5000, 10000)
    # good
    print('card4 balance:', card_4.get_balance())
    print('card5 balance:', card_5.get_balance())
