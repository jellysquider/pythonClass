# Design a class named StopWatch. The class contains:

# The private data fields startTime and endTime with get methods.

# A constructor that initializes startTime with the current time.

# A method named start() that resets the startTime to the current time.
# A method named stop() that sets the endTime to the current time.

# A method named getElapsedTime() that returns
# the elapsed time for the stopwatch in milliseconds.

# Write a test program that measures the execution time
# of adding numbers from 1 to 1,000,000.
import time


class StopWatch:

    def __init__(self):
        self.__startTime = time.time();

    def getStartTime(self):
        return self.__startTime;

    def getEndTime(self):
        return self.__endTime;

    def start(self):
        return self.__startTime;

    def stop(self):
        self.__endTime = time.time();
        return self.__endTime;

    def getElapsedTime(self):
        elapsedTime = self.__endTime - self.__startTime;
        return elapsedTime;


def main():
    task = StopWatch();

    print("Started counting...");
    print("Current time: ", task.start())

    for i in range(1, 1000000):
        i += 1;

    print("Finished counting!");
    print("Current time: ", task.stop())
    print("Execution time: ", task.getElapsedTime());


main();
