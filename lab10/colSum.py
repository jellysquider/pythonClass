# Write a function that returns the sum of all the elements in a specified column
# in a matrix using the following header:
# def sumColumn(m, columnIndex):
#
# Write a test program that reads a 3 * 4 matrix and displays the sum of each col.

def getMatrix():
    matrix = []; # initialize empty matrix

    # get user's input
    input0 = input("Enter a 3-by-4 matrix row for row 0: ");
    input1 = input("Enter a 3-by-4 matrix row for row 1: ");
    input2 = input("Enter a 3-by-4 matrix row for row 2: ");

    # get rid of white spaces
    lst0 = input0.split();
    lst1 = input1.split();
    lst2 = input2.split();

    # turn into integers
    row0 = [eval(x) for x in lst0];
    row1 = [eval(x) for x in lst1];
    row2 = [eval(x) for x in lst2];

    for i in range(1):
        for j in range(1):
            matrix.append(row0);
            matrix.append(row1);
            matrix.append(row2);

    return matrix;


def sumColumn(matrix, columnIndex):
    total = 0;
    # at most 4 cols, j = 0, 1, 2, 3;
    # for each col, j stays the same while i is iterating through rows
    for i in range(3):
        total += matrix[i][columnIndex];

    return total;


def main():
    m = getMatrix();
    # print(m);

    print("Sum of the elements for column 0:", "{0:.1f}".format(sumColumn(m, 0)));
    print("Sum of the elements for column 1:", "{0:.1f}".format(sumColumn(m, 1)));
    print("Sum of the elements for column 2:", "{0:.1f}".format(sumColumn(m, 2)));
    print("Sum of the elements for column 3:", "{0:.1f}".format(sumColumn(m, 3)));

main();
