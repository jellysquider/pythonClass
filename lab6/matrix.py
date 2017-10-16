from random import randint

n = eval(input("Enter n: "))

def printMatrix(n):
    numberOfEntries = n * n + (n - 1);
    i = 0;
    for entry in range(0, numberOfEntries):
        i += 1;
        entry = randint(0,1);
        if (i <= n):
            print(entry, end = " ");
        else:
            i = 0;
            print();
    print();

printMatrix(n);
