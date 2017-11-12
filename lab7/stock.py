# Design a class named Stock to represent a company’s stock that contains:

# A private string data field named symbol for the stock’s symbol.
# A private string data field named name for the stock’s name.
# A private float data field named previousClosingPrice that stores the stock price for the previous day.
# A private float data field named currentPrice that stores the stock price for the current time.

# A constructor that creates a stock with the specified symbol, name, previous price, and current price.

# A get method for returning the stock name.
# A get method for returning the stock symbol.
# Get and set methods for getting/setting the stock’s previous price.
# Get and set methods for getting/setting the stock’s current price.

# A method named getChangePercent() that returns
# the percentage changed from previousClosingPrice to currentPrice.


# Write a test program that creates a Stock object with the stock symbol INTC,
# the name IntelCorporation, the previous closing price of 20.5, and the new current price of20.35,
# and display the price-change percentage.


class Stock:

    def __init__(self, symbol, name, previousClosingPrice, currentPrice):
        self.__symbol = symbol;
        self.__name = name;
        self.__previousClosingPrice = previousClosingPrice;
        self.__currentPrice = currentPrice;

    def getName(self):
        return self.__name;

    def getSymbol(self):
        return self.__symbol;

    def getPreviousClosingPrice(self):
        return self.__previousClosingPrice;

    def setPreviousClosingPrice(self, previousClosingPrice):
        self.__previousClosingPrice = previousClosingPrice;

    def getCurrentPrice(self):
        return self.__currentPrice;

    def setCurrentPrice(self, currentPrice):
        self.__currentPrice = currentPrice;

    def getChangePercent(self):
        decrease = self.__previousClosingPrice - self.__currentPrice;
        return decrease / self.__previousClosingPrice * 100;


def main():
    stock1 = Stock("INTC", "IntelCorporation", 20.5, 20.35);

    print("Price-Change Percentage: {:.2f}%".format(stock1.getChangePercent()))

main();
