# Write a function that returns the index of the smallest element in a list of ints.
# If the number of such elements is greater than 1, return the smallest index.
# Use the following header:
# def indexOfSmallestElement(lst):
#
# Write a test program that prompts the user to enter a list of numbers,
# invokes thisfunction to return the index of the smallest element,
# and displays the index.


s = input("Enter some ints between 1 and 100: ");
# Get rid of white spaces
userData = s.split();
# Create a new list with clean data (just ints)
lst = [eval(x) for x in userData];

def indexOfSmallestElement(lst):
    indexOfSmallest = 0;
    for i in range(len(lst)):
        if lst[i] < lst[indexOfSmallest]:
            indexOfSmallest = i;
    return indexOfSmallest;

print(indexOfSmallestElement(lst));
