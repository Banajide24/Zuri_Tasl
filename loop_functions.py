# This Python progamme registers users with the following details:
# - first name, last name, password, email
# - and generates user account number
# ...................................................
# Registered users can login and validated with their 
# - account number & password
#....................................................
# After successful login, users can navigate to perform bank operations of their choice

# Initializing the system
import random
import validation
import database
from getpass import getpass


def init():
    print("Welcome to GnGBank")

    account_enq = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if account_enq == 1:

        login()

    elif account_enq == 2:

        register()

    else:
        print("You have selected invalid option")
        init()


def login():
    print("********* LOGIN ***********")

    user_account_number = input("What is your account number? \n")

    is_valid_account_number = validation.account_number_validation(user_account_number)

    if is_valid_account_number:

        password = getpass("What is your password \n")

        user = database.authenticated_user(user_account_number, password);

        if user:
            bank_operation(user)

        print('Invalid account or password')
        login()

    else:
        print("Account Number Invalid: Account Number must be 10 digits INTEGERS only")
        init()


def register():
    print("****** WELCOME TO REGISTRATION HANDLE *******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = getpass("Create a STRONG password for yourself \n")

    account_number = generation_account_number()

    is_user_created = database.create(account_number, first_name, last_name, email, password)

    if is_user_created:

        print("Your Account Has been created")
        print(" == ==== ====== ===== ===")
        print("Your account number is: %d" % account_number)
        print("Make sure you keep it safe")
        print(" == ==== ====== ===== ===")

        login()

    else:
        print("Something went wrong, please try again")
        register()


def bank_operation(user):
    print("Welcome %s %s " % (user[0], user[1]))

    selected_option = int(input("What OPERATION would you like to do? (1) DEPOSIT (2) WITHDRAWAL (3) COMPLAINT (4) LOGOUT (5) EXIT \n"))

    if selected_option == 1:

        deposit_operation()
    elif selected_option == 2:

        withdrawal_operation()
    elif selected_option == 3:

        complaint()
    elif selected_option ==4:
        
        logout()
    elif selected_option == 5:

        exit()
        print('Thank you for banking with us')
    else:

        print("Invalid option selected")
        bank_operation(user)


def withdrawal_operation():
    print("withdrawal")
    # get current balance
    # get amount to withdraw
    # check if current balance > withdraw balance
    # deduct withdrawn amount form current balance
    # display current balance


def deposit_operation():
    print("Deposit Operations")
    # get current balance
    # get amount to deposit
    # add deposited amount to current balance
    # display current balance

def complaint():
    print('you selected \s', selectedOption)
    complaint = input('What issue will you like to report? \n')
    print('Thank you for contacting us')

def generation_account_number():
    return random.randrange(1111111111, 9999999999)


def set_current_balance(user_details, balance):
    user_details[4] = balance


def get_current_balance(user_details):
    return user_details[4]


def logout():
    login()


init()
