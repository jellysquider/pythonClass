# Write a program that reads some integers between 1 and 100
# and counts the occurrences of each.
s = input("Enter some ints between 1 and 100: ");
# Get rid of white spaces
userData = s.split();
# Create a new list with clean data (just ints)
nums = [eval(x) for x in userData if eval(x) >= 1 and eval(x) <= 100];
nums.sort();

# initialize and later create a new list w/o duplicates
tmp = [];
# create len ints with initial value 0
counts = (len(nums)) * [0];

for i in nums:
  if i not in tmp:
    tmp.append(i);
tmp.sort();

def countNums(nums):
    # for each int in the list, count it
    for i in range(len(tmp)):
        counts[i] = nums.count(tmp[i]);
    return counts;

def printCounts(counts):
    for i in range(len(tmp)):
        if(counts[i] == 1):
            print(tmp[i]," occurs 1 time");
        else:
            print(tmp[i], " occurs ", counts[i], " times");

print("The occurences of each number are: ");
countNums(nums);
printCounts(counts);
