# Problem Statement
#Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):

#There are 5 seconds in a year!

#Solution :

DAYS_PER_YEAR: int = 365
HOURS_PER_DAY: int = 24
MIN_PER_HOUR: int = 60
SEC_PER_MIN: int = 60

def main():
    SEC_IN_YEAR: int = DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN
    print("There are " + str(SEC_IN_YEAR) + " seconds in a year!")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
