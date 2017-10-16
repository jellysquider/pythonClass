# Write a function that displays an n-by-n matrix using the following header:
# def printMatrix(n): Each element is 0 or 1, which is generated randomly.
# Write a test program that prompts the user to enter n and displays an n-by-n matrix.


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
