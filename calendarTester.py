#!/usr/bin/python
import datetime
import sys
from convertToCalendar import convertToCalendar
import difflib #library for comparing differences

# runs tests for convertToCalendar function
def calendarTest():

    #hardcoded sample tests
    testEvents = ["Engineers on the Green Engineering Organization Fair Monday, September 30, 2020 2pm - 6pm * Warren Mall","ACM EATS @ IN-N-OUT 10/03/20 @ 9:00pm 2910 Damon Ave, San Diego, CA 92109", "ACM x TSE Advanced C++ Workshops November 8 & 15 6:30-9 pm tsa.ucsd.edu", "" ]

    test = []
    test_name = []

    today = datetime.datetime.today()

    #setting datetime objects for sample test solutions
    test1 = datetime.datetime(2020, 9, 30, 14, 0, 0 )
    test2 = datetime.datetime(2020, 10, 3, 21, 0, 0 )
    test3 = datetime.datetime(2021, 11, 8, 18, 30, 0 )
    test4 = datetime.datetime(today.year, today.month, today.day, 0, 0, 0 )
    test.append(test1)
    test.append(test2)
    test.append(test3)
    test.append(test4)

    #setting eventNames for tests
    test_name.append("Engineers on the Green Engineering Organization Fair")
    test_name.append("ACM EATS @ IN-N-OUT")
    test_name.append("ACM x TSE Advanced C++ Workshops")
    test_name.append("")

    #compare the expected test results with the actual
    for i in range(len(testEvents)):
        temp1, temp2 = convertToCalendar(testEvents[i])
        print("Expected date: " + test[i].strftime("%m/%d/%Y, %H:%M"))
        print("Expected name: " + test_name[i])
        print("calendarTest date: " + temp1.strftime("%m/%d/%Y, %H:%M"))
        print("calendarTest name: " + temp2)

if __name__ == '__main__':
    calendarTest()
