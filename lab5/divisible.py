count = 100;
# while (count <= 200):
print("The integers that are divisible by 5 or 6 are: ")
for count in range(201):
    if ((count % 5 == 0) or (count % 6 == 0)):
        print(format(count, "5d"), end = '');
    #print 10 numbers per line
    if (count % 30 == 0):
        print();
