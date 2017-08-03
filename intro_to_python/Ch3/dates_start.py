#
# Example file for working with date information
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

from datetime import date
from datetime import time
from datetime import datetime

def main():
    # today = date.today()
    # print   "the date is ", today
    # print "the date components are ", today.day, today.month,today.year
    # print "today's date number is ", today.weekday()

    today = datetime.now()
    print   "the date is ", today
    print 'the current time is ', datetime.time(today)

if __name__ == "__main__":
  main();
