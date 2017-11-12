# design a class named Rectangle to represent a rectangle.
# The class contains:
# Two data fields named width and height.
# A constructor that creates a rectangle with the specified width and height (def: 1 and 2)
# A method named getArea() that returns the area of this rectangle.
# A method named getPerimeter() that returns the perimeter.
#
# Write a test program that creates two Rectangle objects
# —one with width 4 and height 40
# and the other with width 3.5 and height 35.7.
#
# Display the width, height, area, and perimeter of each rectangle in this order.

class Rectangle:

    def __init__(self, width = 1, height = 2):
        self.width = width;
        self.height = height;

    def getPerimeter(self):
        return 2 * (self.width + self.height);

    def getArea(self):
        return self.width * self.height;


def main():
    rect1 = Rectangle(4, 40);
    print("Rectangle 1: " + "\nwidth", rect1.width, "\nheight",rect1.height,
    "\nArea",rect1.getArea(), "\nPerimeter", rect1.getPerimeter())

    print("--------------")


    rect2 = Rectangle(3.5, 35.7);
    print("Rectangle 2: " + "\nwidth", rect2.width, "\nheight",rect2.height,
    "\nArea",rect2.getArea(), "\nPerimeter", rect2.getPerimeter())

main();
