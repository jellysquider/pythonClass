# Write a program that reads in numbers separated by a space in one line
# and displays distinct numbers (i.e., if a number appears multiple times,
# it is displayed only once).
#
# (Hint: Read all the numbers and store them in list1.
# Create a new list list2. Add a number in list1 to list2.
# If the number is already in the list, ignore it.)

s = input("Enter some numbers: ");
# Get rid of white spaces
userData = s.split();
# Create a new list with clean data (just ints)
list1 = [eval(x) for x in userData];
list2 = [];

for i in list1:
  if i not in list2:
    list2.append(i);

print("The distinct numbers are:", end=' ');
for x in range(len(list2)):
    print(list2[x], end=' ');
