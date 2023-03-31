#simple password generator in python

# Import the required modules
import random
import string

# Define a function to generate a password
def genPass():
    # Initialize an empty string to hold the password
    password = ''
    # Generate a random password of length between 10 and 20 characters
    for i in range(random.randint(10, 20)):
        # Append a random character to the password string
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    # Return the generated password
    return password

# Define a main function to handle user input
def main():
    # Ask the user what they would like to do
    choice = input('What would you like to do? \n(1) Generate Password \n(2) Exit \n>')
    # If the user chooses to generate a password, call the genPass function and print the result
    if choice == '1':
        # Ask the user how many passwords they want to generate
        num_passwords = int(input('How many passwords would you like to generate? \n>'))
    # Generate the specified number of passwords and print them out
        for i in range(num_passwords):
            print(genPass())
    # If the user chooses to exit, print a goodbye message and exit the program
    elif choice == '2':
        print('Goodbye!')
        exit()
    # If the user enters an invalid choice, print an error message and call the main function again
    else:
        print('Invalid Choice')
        main()

# If this script is being run as the main program, call the main function
if __name__ == '__main__':
    main()

# Author: @Loocist23
# Path: GenPassPy.py
