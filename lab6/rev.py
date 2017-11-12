# Write the following function to display an integer in reverse order:
# def reverse(number): For example, reverse(3456) displays 6543.
# Write a test program that prompts the user to enter an integer
# and displays its reversal.


number = eval(input("Enter the number: "));
def reverse(number):
    reverse = 0;
    while(number != 0):
        reverse *= 10;
        reverse += number % 10;
        number //= 10;
    print(reverse);

reverse(number);
