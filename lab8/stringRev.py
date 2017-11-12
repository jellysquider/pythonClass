# Write a function that reverses a string.
# The header of the function is: def reverse(s):
# Write a test program that prompts the user to enter a string,
# invokes the reverse function, and displays the reversed string.

def reverse(s):
    length = len(s);
    i = length - 1;
    while(i >= 0):
        print(s[i], end = '');
        i -= 1;
    return '';


def main():
    s = str(input("Enter a string to be reversed: "));

    rev = reverse(s);
    print(rev);

main();
