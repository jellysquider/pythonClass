a = eval(input("Enter the first integer: "));
b = eval(input("Enter the second integer: "));
c = eval(input("Enter the third integer: "));

if (a < c and a < b and c < b):
    print("The order is: ", a, c, b);
elif (a < c and a < b and b < c):
    print("The order is: ", a, b, c);
elif (a > b and a > c and b > c):
    print("The order is: ", c, b, a);
elif (a > b and a > c and b < c):
    print("The order is: ", b, c, a);
elif (b > c and b > a and a > c):
    print("The order is: ", c, a, b);
elif (c > b and c > a and a > b):
    print("The order is: ", b, a, c);
