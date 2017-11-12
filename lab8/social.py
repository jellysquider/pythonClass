# Write a program that prompts the user to enter a Social Security number
# in the format ddd-dd-dddd, where d is a digit. The program displays
# Valid SSN for a correct Social Security number or Invalid SSN otherwise.


def main():
    SSN = str(input("Enter a Social Security number in the format ddd-dd-dddd: "));

    if(len(SSN) == 10):
        if (SSN[0:2].isdigit() == True and SSN[3] == '-' \
        and SSN[4:5].isdigit() == True and SSN[6] == '-' \
        and SSN[7:10].isdigit() == True):
            print("Valid SSN");
    else:
        print("Invalid SSN");


main();
