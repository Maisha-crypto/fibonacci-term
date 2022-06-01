import numpy as np


def Fibonacci_Sequence(user_number):
    last_term = 1 
    second_last_term = 0
    exit_loop = False

    if user_number == 0:
        print("An intiger can't have 0 digits")
    elif user_number < 0:
        print("Please enter a positive intiger > 0")
    elif user_number == 1:
        counter = 1
        print(counter)
    else:
        counter = 1
        while exit_loop != True:
            current_term = second_last_term + last_term
            second_last_term = last_term
            last_term = current_term
            counter = counter+1

            if user_number == Get_Number_of_Digits(current_term):
                exit_loop = True
        print(counter)


def Get_Number_of_Digits(number_):

    if number_ < 0:
        print("Please Enter Positive Number")

    elif number_ == 0:
        print("Please enter a positive integer")

    elif number_ > 0:
        number_of_digits = int(np.log10(number_))+1

    return number_of_digits

    
if __name__ == "__main__":

    input_number = input("")

    try:
        intiger_check = int(input_number)
        Fibonacci_Sequence(intiger_check)   
    except ValueError:
        print("Invalid input, Please enter an intiger value!!")


    