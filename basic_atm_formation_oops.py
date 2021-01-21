class Atm:
    def __init__(self,pin,balance):
        self.pin=""
        self.balance=0

        self.menu()

    def menu(self):
        user_input=input("""
                            How would you like to proceed?
                            1.Enter 1 to create your pin
                            2.Enter 2 to deposit
                            3.Enter 3 to withdraw
                            4.Enter 4 to check balance
                            5.Enter 5 to exit
                            """)
    if user_input=="1":
        self.create_pin()
    elif user_input=="2":
        self.deposit()
    elif user_input=="3":
        self.withdraw()
    elif user_input=="4":
        self.check_balance()
    elif user_input=="5":
        print("over")

    def create_pin(self):
        self.pin=input("enter your pin")
        print("pin set over")
    def depoit(self):
        temp=input("enter your pin")
        if temp==sel.pin:
            amount=int(input("enter your amount"))
            self.balance=self.balnce+amount
            print("amount deposited")
        else:
            print("incorrect pin")
    def withdraw(self):
        temp=input("enter your pin")
        if temp==self.pin:
            amount=int(input("enter your amount"))
            if amount<self.balance:
                self.balance=self.balnce-amount
                print(f"{amount} amount is withdraw")
            else:
                print("required amount is not available")
        else:
            print("incorrect pin")
    def check_balance(self):
        temp=input("enter your pin")
        if temp==self.pin:
            print(f"balance is{self.balance}")
        else:
            print("incorrect pin")
    



        
