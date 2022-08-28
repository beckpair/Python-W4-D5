class Rental():
    def __init__(self):
        self.income = 0,
        self.expenses = 0,
        self.investment = 0
        self.annualCashFlow = 0
        self.returnOnInvestment = 0

    def totalIncome(self):
        while True:
            income = int(input(f"Please enter any income you receive from this property per month. Remember to include things like: \n Rent \n Parking spots \n Laundry \n Pets \n etc. \n\n "))
            self.income = income
            break
                        
    def totalExpenses(self):
        while True:
            expenses =  int(input(f"Please enter any expenses you pay on this property per month. Remember to include things like: \n Mortgage payments \n Utilities \n Taxes \n Insurance \n Repairs \n Capital Expenditures \n etc. \n\n"))           
            self.expenses = expenses
            break
            
    def totalInvestment(self):
        while True:
            investment = int(input(f"Please input any monetary investment you made in the property. Include things like: \n Down payment \n Closing Costs \n Renovation Costs \n\n  "))
            self.investment = investment  
            break



# class Finance(Rental):
    def __init__(self):
        self.annualCashFlow = 0
        self.returnOnInvestment = 0

    def cashFlow(self):
        monthly = self.income - self.expenses
        self.annualCashFlow = monthly * 12
        seeIt = input("Would you like to see your annual cash flow? Y/N ")
        if seeIt.lower() in ('y', 'yes'):
            print(f"Your annual cash flow is ${self.annualCashFlow}.")
        
    
    def returns(self):
        roi = self.annualCashFlow / self.investment
        self.returnOnInvestment = roi * 10
        print(f"Your cash-on-cash ROI is {self.returnOnInvestment}%.")

my_rental = Rental()

def run():
    user_input = input("""
    Hello! Welcome to our ROI calculator. Please complete the following program in order to calculate your estimated return on investment.
    Step 1) Input total income
    Step 2) Input total expenses
    Step 3) Input total investment
    Step 4) Calculate cash flow
    Step 5) Calculate ROI
    
    Enter 'Start' to start the program!

    """)

    while True:
        if user_input.lower() == "start":

            my_rental.totalIncome()

            my_rental.totalExpenses()

            my_rental.totalInvestment()

            my_rental.cashFlow()
    
            my_rental.returns()
        
            print("Thank you for using our program!")
            break
        else:
            print("Please enter 'Start' to start the program.")

        
run()

