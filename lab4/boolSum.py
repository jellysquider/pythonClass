from random import randint

int1 = randint(0, 100);
int2 = randint(0, 100);
intSum = int1 + int2;


print("The first integer is:", int1)
print("The second integer is:", int2)
result = eval(input("Enter the sum of two integers:"));

print("Your result is: ", result == intSum)
