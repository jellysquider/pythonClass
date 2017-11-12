# Some Web sites impose certain rules for passwords.
# Write a function that checks whether a string is a valid password.
#
# Suppose the password rules are as follows:
# A password must have at least eight characters.
# A password must consist of only letters and digits.
# A password must contain at least two digits.
#
# Write a program that prompts the user to enter a password
# and displays valid password if the rules are followed
# or invalid password otherwise.

def checkPassword(password):
    length = len(password);
    count = 0;
    for i in range(0, length):
        if (password[i].isdigit() == True):
            count += 1;
    if(length >= 7 and password.isalnum() == True and count >= 2):
        return "valid password";
    else:
        return "invalid password";


def main():
    password = str(input("Create a password: "));

    print(checkPassword(password));


main();
