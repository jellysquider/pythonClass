value = eval(input("Enter an integer, the input ends if it's 0: "));

total = 0;
negative = 0;
positive = 0;
while (value != 0):
    if (value < 0):
        negative += 1;
    else:
        positive += 1;
    total += value;
    number_of_ints = negative + positive;
    average = total / number_of_ints;
    # keep reading data until input is zero
    value = eval(input("Enter an integer, the input ends if it's 0: "));
print("The number of positives is: ", positive);
print("The number of negatives is: ", negative);
print("The total is: ", total);
print("The average is: ", average);
