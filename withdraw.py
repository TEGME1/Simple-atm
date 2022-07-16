import account


class WITHDRAW:
    def __init__(self, acc_no, amt):
        self.acc_no = acc_no
        self.amt = amt

    def withdraw(self, printText=False):
        acc = account.ACCOUNT(self.acc_no)
        if acc.fetchBalance() > 2000:
            if self.amt < acc.fetchBalance() and self.amt < 200000:
                balance = acc.fetchBalance() - self.amt
                acc.updateBalance(balance)
                if printText:
                    print("The Money Has Been Withdrawn")
                    print(f"The Money Withdrawn : {self.amt}")
        else:
            print("Not Enough Money")
