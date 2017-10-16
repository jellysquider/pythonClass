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
