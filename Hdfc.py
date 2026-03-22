class Hdfc:
    ROI = 9.5       #Class variable

    def __init__( self, strName, intAmount ):       # Constructor
        self.intBalance = intAmount                 # Instance Variable
        self.strAccountHolder = strName             # Instance Variable
        print("Welcome", self.strAccountHolder )
        print("Account get successfully created with initial Balance : ", self.intBalance )

    def DisplayBalance(self):                       # Instance Method
        print("Hello", self.strAccountHolder)
        print( "Your Account Balance is : ", self.intBalance )

    def Withdraw(self, intAmount ):                 # Instance Method
        if self.intBalance < intAmount:
            print( "Sorry, You have insufficient balance" )
        else:
            self.intBalance = self.intBalance - intAmount
            print( "Amount withdraw successfully.." )

    def Deposit(self, intAmount):                   # Instance Method
        self.intBalance = self.intBalance + intAmount
        print( "Amount deposited successfully, current balance is : ", self.intBalance )

    @classmethod
    def DisplayBankInfo(cls):                       # Class Method
        print("Welcome to HDFC Bank portal")
        print("We provide the Rate of Interest on save account ", cls.ROI)

    @classmethod
    def CreateAccount(cls):
        print()
        print("Creating new account: ")

    @staticmethod
    def DisplayKYCInfo():
        print("According to the rules of RBI you should provide below documents for KYC:")
        print("Your Aadhar Card")
        print("Your PAN Card")
        print("Your Passport Size Photo")    

def main():
    Hdfc.DisplayBankInfo()                          # Without creating object we can call class method
    print("ROI of HDFC Bank : ", Hdfc.ROI )         # Without creating object we can call class variable
    Hdfc.DisplayKYCInfo()                           # Without creating object we can call static method

    Hdfc.CreateAccount()
    objAnand = Hdfc( "Anand", 50000 )               # __init__(100, "Anand", 50000 )
    print("Performing operations on ", objAnand.strAccountHolder + "'s Account: ")
    objAnand.DisplayBalance()
    objAnand.Withdraw(100)
    objAnand.DisplayBalance()
    objAnand.Deposit(1000)
    objAnand.DisplayBalance()

    Hdfc.CreateAccount()
    objAnvit = Hdfc( "Anvit", 5000 )                # __init__(200, "Anvit", 5000 )
    print("Performing operations on ", objAnvit.strAccountHolder + "'s Account: ")
    objAnvit.DisplayBalance()
    objAnvit.Withdraw(20)
    objAnvit.DisplayBalance()
    objAnvit.Deposit(150)
    objAnvit.DisplayBalance()

    # Negative scenario
    objAnvit.Withdraw(10000)

if __name__ == "__main__":
    main()