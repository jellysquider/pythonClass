# Write a function that prints characters using the following header:
# def printChars(ch1, ch2, numberPerLine): This function prints the characters
# between ch1 and ch2 with the specified numbers per line.
# Write a test program that prints ten characters per line from 1 to Z.


def printChars(ch1, ch2, numberPerLine):
    i = 0;
    for entry in range(ord(ch1), ord(ch2) + 1):
        i += 1;
        if (i < numberPerLine):
            print(chr(entry), end = " ");
        else:
            i = 0;
            print();
    print();

printChars('1', 'Z', 10);
