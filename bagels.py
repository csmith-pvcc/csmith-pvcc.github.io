# Name: Chapman Smith
#Prog Purose: This program finds the cost of movie tickets
#   Price for one ticket: $10.99
#   Sales tax rate: 5.5%

import datetime

############## define global variables ##############
# define tax rate and prices
SALES_TAX_RATE = .06
PR_BAGEL = 2.25
PR_CREAMCH = 1.25

# define global variables
num_bagels = 0
num_creamch = 0
cost_bagels = 0
subtotal = 0
sales_tax = 0
total = 0

############## define program functions ##############
def main ():
        get_user_data()
        perform_calculations()
        display_results()

def get_user_data():
    global num_bagels, num_creamch
    num_bagels = int(input("Number of bagels: "))
    num_creamch = int(input("Number of cream cheese:"))

def perform_calculations():
    global cost_bagels, cost_creamch, subtotal, sales_tax, total
    cost_bagels = num_bagels * PR_BAGEL
    cost_creamch = num_creamch * PR_CREAMCH
    subtotal, sales_tax, total
    subtotal = num_tickets * PR_TICKET
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_results():
    print ('------------------------------------')
    print ('**** Brownsville Bagel Company ****')
    print ('Fresh-baked bagels ever day!')
    print (' -----------------------------------')
    print ('Bagels    $ ' + format (cost_bagels,'8,.2f'))
    print ('Cream Cheese $ ' + str(cost_creamch))
    print ('-------------------------------------')
    print ('Subtotal   $ ' + str(subtotal))
    print ('Sales Tax  $ ' + str(sales_tax))
    print ('Total      $ ' + str(total))
    print (' ------------------------------------')
    print (str(datetime.datetime.now()))

########## call on main program to execute #########
main()
