amount = input("Please ented the desired amount to withdraw / deposit : ")
class Atm(object):
    
    def __init__(self,username,cardnumber,pinnumber,amount):
        self.username = username
        self.cardnumber = cardnumber 
        self.pinnumber = pinnumber

    def CashWithdrawal(self):
        print("You have successfully withdrawn", amount, "amount of money!")

    def BalanceEnquiry(self):
        print("You have 10,000 INR in the bank!")

    def DepositCash(self):
        print("You have successfully deposited ", amount, "amount of money!")

UserKushaan = Atm("Kushaan Agarwal", "1234 5678 9101112", "1234", amount)
UserKushaan.CashWithdrawal()
UserKushaan.BalanceEnquiry()
UserKushaan.DepositCash()
print("Card Number : " + UserKushaan.cardnumber)
