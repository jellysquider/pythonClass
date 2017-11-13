# Write a program that reads an unspecified number of scores
# and determines how many scores are above or equal to the average
# and how many scores are below the average.
# Assume the input numbers are separated by one space in one line.

userData = input("Enter the scores: ");

lst = userData.split();
scores = [eval(x) for x in lst];

total = 0;
for i in range(0, len(scores)):
    total += scores[i];
average = round(total / (len(scores)));
print("Average score is: ", average);

aboveAverage = 0;
belowAverage = 0;
for i in range(0, len(scores)):
    if (scores[i] >= average):
        aboveAverage += 1;
    else:
        belowAverage += 1;

print("There are ", aboveAverage, " above or equal to average score(s)");
print("There are ", belowAverage, " below average score(s)");
