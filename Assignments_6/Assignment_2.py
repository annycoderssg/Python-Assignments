class BankAccount:
    fltROI = 10.5

    def __init__(self, strName, fltAmount ):
        self.strName = strName
        self.fltAmount = fltAmount

    def Display(self):
        print("Name: ", self.strName )
        print("Amount: ", self.fltAmount )

    def Deposit(self, fltAmount):
        self.fltAmount = self.fltAmount + fltAmount

    def Withdraw(self, fltAmount):
        self.fltAmount = self.fltAmount - fltAmount

    def CalculateInterest(self, intNumberOfMonths):
        self.fltAmount += (self.fltAmount * BankAccount.fltROI * intNumberOfMonths) / 100

def main():
    objBankAccount1 = BankAccount( "Anand Shinde", 50000 )
    objBankAccount1.Deposit( 2500 )
    objBankAccount1.Withdraw( 5250 )
    objBankAccount1.CalculateInterest( 12 )
    objBankAccount1.Display()

    objBankAccount2 = BankAccount( "Anvit Shinde", 10000 )
    objBankAccount2.Deposit( 2000 )
    objBankAccount2.Withdraw( 3000 )
    objBankAccount2.CalculateInterest( 36 )
    objBankAccount2.Display()

if __name__ == "__main__":
    main()