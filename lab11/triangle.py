from GeometricObject import GeometricObject
from math import sqrt



class Triangle(GeometricObject):
    def __init__(self, side1 = 1.0, side2 = 1.0, side3 = 1.0):
        super().__init__();
        self.__side1 = side1;
        self.__side2 = side2;
        self.__side3 = side3;


    def getSide1(self):
        return self.__side1;

    def getSide2(self):
        return self.__side2;

    def getSide3(self):
        return self.__side3;

    

    def getArea(self):
        self.__s = (self.__side1 + self.__side2 + self.__side3) / 2;
        self.__area = sqrt( self.__s*(self.__s - self.__side1)*(self.__s - \
                        self.__side2)*(self.__s - self.__side3) );
        return self.__area;


    def getPerimeter(self):
        self.__perimeter = self.__side1 + self.__side2 + self.__side3;
        return self.__perimeter;

    def __str__(self):
        return "color: " + str(self.__side2) + \
                " and filled: " + str(self.__side1)


    def __str__(self):
        return "Triangle: side1 = " + str(self.__side1) + " side2 = " + str(self.__side2) + \
                " side3 = " + str(self.__side3);

def main():
    side1 = eval(input("Enter dimensions of side1: "));
    side2 = eval(input("Enter dimensions of side2: "));
    side3 = eval(input("Enter dimensions of side3: "));
    newColor =  input("Enter color of the triangle: ");
    fill = int(input("Enter 0 for not filled and 1 for filled triangle: "));

    newTriangle = Triangle(side1, side2, side3);
    newTriangle.setColor(newColor);
    newTriangle.setFilled(fill);

    # print("A triangle", newTriangle)
    print("\nArea of the triangle: ", newTriangle.getArea());
    print("Perimeter of the triangle: ", newTriangle.getPerimeter());
    print("Color of the triangle: ", newTriangle.getColor())
    print("Is triangle filled? ", bool(newTriangle.isFilled()));

main();
