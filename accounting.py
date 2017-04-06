melon_cost = 1.00

def check_payment(file_name):
    """ Checks to see if customer list paid correctly """
    payment_file = open(file_name)

    for line in payment_file:
        line = line.rstrip()
        customer_payment_info = line.split("|") #tokenizes string

        check_info(customer_payment_info) #calls the check info function

    payment_file.close()

def check_info(payment_info):
    """ Checks each customer line and prints our incorrect payment """
    expected_payment = float(payment_info[2]) * melon_cost
    customer_payment = float(payment_info[3])
    customer_name = payment_info[1]

    #checking if expected and real payments
    if expected_payment < customer_payment:

        print customer_name, "paid {:.2f}, expected {:.2f}".format(
            customer_payment, expected_payment)
        print customer_name, "has paid too much for their melons."

    elif expected_payment > customer_payment:
        print customer_name, "paid {:.2f}, expected {:.2f}".format(
            customer_payment, expected_payment)
        print customer_name, "has paid too little for their melons."

check_payment("customer-orders.txt")
