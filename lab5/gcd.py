n1 = eval(input("Enter the first integer: "));
n2 = eval(input("Enter the second integer: "));

gcd = 1;

# finding min of two
if (n1 < n2):
    d = n1;
else:
    d = n2;

for d in range(d, 0, -1):
    if ((n1 % d == 0) and (n2 % d == 0)):
        gcd = d;
        break;
print("The GCD is: ", gcd);
