number = eval(input("Enter a number between 1 and 1000: "));

# % - extract a digit
# // - remove the extracted
outerRight = number % 10;
middle = (number % 100) // 10;
outerLeft = number // 100;

digitSum = outerRight + middle + outerLeft;

print("The sum of the digits is: ", digitSum);
