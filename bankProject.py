class AccountDetails:
    _person_info = {}
    def __init__(self):
        print("entered in my account once")
class PersonBankDetails(AccountDetails):
    def createAccount(self, name, account_number, user_name, password):
        super()._person_info[user_name] = {"name":name, "account_number": account_number, "password":password, "balance":0}
    def accountLogin(self, user_name, password):
        login_status = 0
        try:
            if super()._person_info[user_name]["password"] == password:
                print("Login Success")
                login_status = True
            else:
                print("Login Failured. please try again")
                login_status = False
        except:
            print("Exception: Login Failured. please try again")
            login_status = False
        return login_status
    def amountWithdrawal(self,user_name, amount):
        if amount > super()._person_info[user_name]["balance"]:
            print("Sorry! Balance Insuffient")
        else:
            super()._person_info[user_name]["balance"] = super()._person_info[user_name]["balance"]-amount
            print("Withdrawal Success.Current balance:", super()._person_info[user_name]["balance"])
    def amountDeposit(self,user_name, amount):
        super()._person_info[user_name]["balance"] +=amount
        print("Deposited successfully!Current balance:", super()._person_info[user_name]["balance"])

print("Starting the Banking Project")
p = PersonBankDetails()

while True:
    first = int(input("Select \n1. Create new Account \n2.Login\n3.Quit\n>"))
    match(first):
        case 1:
            print("Creating new account")
            name = input("Please Enter name:")
            account_number = int(input("Enter Account number:"))
            user_name = input("Enter User Name:")
            password = input("Enter Password:")
            p.createAccount(name, account_number, user_name, password)
        case 2:
            print("login!")
            user_name = input("Enter User Name:")
            password = input("Enter Password:")
            if (p.accountLogin(user_name,password)==True):
                action_selection = int(input("1. withdrawal\n2.deposit"))
                match(action_selection):
                    case 1:
                        amount = float(input("Enter the amount:"))
                        p.amountWithdrawal(user_name, amount)
                    case 2:
                        amount = float(input("Enter the amount:"))
                        p.amountDeposit(user_name, amount)
        case 3:
            break

