# Write a program that randomly fills in 0s and 1s into a 4 * 4 matrix,
# prints the matrix, and finds the rows and columns with the most 1s.

from random import randint

# empty list
matrix = []

for i in range(4):
    matrix.append([]);
    for j in range(4):
        matrix[i].append(randint(0,1));
        print(matrix[i][j], end=' ');
    print();

# for i in range(4):
#     for j in range(4):
#         if(matrix[i][j] == 1):
#             rowCount += 1;
