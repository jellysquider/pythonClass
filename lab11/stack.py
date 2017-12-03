class Stack(list):
    def __init__(self):
        self.__elements = [];


def main():
    str0 = input("Enter string 0: ");
    str1 = input("Enter string 1: ");
    str2 = input("Enter string 2: ");
    str3 = input("Enter string 3: ");
    str4 = input("Enter string 4: ");

    newStack = Stack();

    newStack.append(str0);
    newStack.append(str1);
    newStack.append(str2);
    newStack.append(str3);
    newStack.append(str4);

    print(newStack)

    newStack.reverse()

    print(newStack)



main();
