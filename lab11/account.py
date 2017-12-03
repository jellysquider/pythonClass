class Account(object):
    def __init__(self, ID = 0, balance = 100.00, annualInterestRate = 0):
        super().__init__();
        self.__ID = ID;
        self.__balance = balance;
        self.__annualInterestRate = annualInterestRate;

    def getID(self):
        return self.__ID;

    def setID(self, ID):
        self.__ID = ID;

    def getBalance(self):
        return self.__balance;

    def setBalance(self, balance):
        self.__balance = balance;

    def getAnnualInterestRate(self):
        return self.__annualInterestRate;

    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate;


    def getMonthlyInterest():
        self.__monthlyInterestRate = (self.__annualInterestRate / 100) / 12;
        return self.__balance * self.__monthlyInterestRate;

def main():
    newAccount = Account();
    newAccount = 10 * [100.00];
    userID = 0;
    while (userID >= 0 and userID <= 9):
        userID = eval(input("Enter an account id: "));
        userChoice = 0;
        while(userChoice != 4):
            print("\nMain Menu:");
            print("1: Check Balance");
            print("2: Withdraw");
            print("3: Deposit");
            print("4: Exit");
            userChoice = int(input("Enter your choice: "));
            if (userChoice == 1):
                print("The balance is: {:.2f}".format(newAccount[userID]));
            elif (userChoice == 2):
                wAmt = int(input("Enter amount to withdraw: "));
                newAccount[userID] = newAccount[userID] - wAmt;
            elif (userChoice == 3):
                dAmt = int(input("Enter amount to deposit: "));
                newAccount[userID] = newAccount[userID] + dAmt;
            elif (userChoice == 4):
                break;

main();
