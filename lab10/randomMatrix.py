# Write a program that randomly fills in 0s and 1s into a 4 * 4 matrix,
# prints the matrix, and finds the rows and columns with the most 1s.

from random import randint

# empty list
matrix = []


# counting lists one for cols, another one for rows
rowCount = 4 * [0];
colToRow = 4 * [0];
colCount = 4* [0];

for i in range(4):
    matrix.append([]);
    for j in range(4):
        matrix[i].append(randint(0,1));
        print(matrix[i][j], end=' ');
    print();

# print(matrix)


def indexOfLargestElement(lst):
    indexOfLargest = 0;
    tmp = [];
    for i in range(len(lst)):
        if lst[i] > lst[indexOfLargest]:
            indexOfLargest = i;
    for i in range(len(lst)):
        if lst[i] == lst[indexOfLargest]:
            tmp.append(i);
    return tmp;



for i in range(4):
    # extract columns and convert them into rows of a different list
    colToRow[i] = [row[i] for row in matrix]
# print(colToRow, end=' ')

# count 1's in each row and add them to lists
rowCount = [row.count(1) for row in matrix]
colCount = [col.count(1) for col in colToRow]
# print("\n", rowCount, end=' ')
# print(colCount, end=' ')

print("The largest row index: ", indexOfLargestElement(rowCount))
print("The largest column index: ", indexOfLargestElement(colCount))
