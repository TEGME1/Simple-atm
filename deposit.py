import account


class DEPOSIT:
    def __init__(self, acc_no, amt):
        self.acc_no = acc_no
        self.amt = amt

    def deposit(self, printText=False):
        acc = account.ACCOUNT(self.acc_no)
        balance = self.amt + acc.fetchBalance()
        acc.updateBalance(balance)
        if printText:
            print("The Money Has Been Deposited")
            print(f"The Money Deposited : {self.amt}")
