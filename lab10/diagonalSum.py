# Write a function that sums all the numbers of the major diagonal
# in an n * n matrix of integers using the following header:
#
# def sumMajorDiagonal(m):
#
# The major diagonal is the diagonal that runs from the top left corner
# to the bottom right corner in the square matrix.
#
# Write a test program that reads a 4 * 4 matrix and displays
# the sum of all its elements on the major diagonal.

def getMatrix():
    matrix = []; # initialize empty matrix

    # get user's input
    input0 = input("Enter a 4-by-4 matrix row for row 0: ");
    input1 = input("Enter a 4-by-4 matrix row for row 1: ");
    input2 = input("Enter a 4-by-4 matrix row for row 2: ");
    input3 = input("Enter a 4-by-4 matrix row for row 3: ");

    # get rid of white spaces
    lst0 = input0.split();
    lst1 = input1.split();
    lst2 = input2.split();
    lst3 = input3.split();

    # turn into integers
    row0 = [eval(x) for x in lst0];
    row1 = [eval(x) for x in lst1];
    row2 = [eval(x) for x in lst2];
    row3 = [eval(x) for x in lst3];

    for i in range(1):
        for j in range(1):
            matrix.append(row0);
            matrix.append(row1);
            matrix.append(row2);
            matrix.append(row3);
    return matrix;


def sumMajorDiagonal(matrix):
    total = 0;
    # at most 4 cols, j = 0, 1, 2, 3;
    # for each col, j stays the same while i is iterating through rows
    for i in range(4):
        j = i;
        total += matrix[i][j];

    return total;


def main():
    m = getMatrix();
    # print(m);

    print("Sum of the elements in the major diagonal is:", "{0:.1f}".format(sumMajorDiagonal(m)));

main();
