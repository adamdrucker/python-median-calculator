# The median is the value at the middle point of a list of numbers
# Arrange the numbers in sequential order, then locate the the value
# in the middle. If there the list is even, and there is no definite
# middle value, add up the two values in the middle and find their mean.


def median():
    # Enter a number, or 'q' to quit
    iVal = input("Enter a number for median calculation (q to quit): ")
    iList = []  # Init empty list
    # Append input to list
    while iVal != 'q':
        iList.append(int(iVal))
        iVal = input("Enter a number for median calculation (q to quit): ")
    # Main stuff
    iLen = len(iList)   # Calculate list length
    iList.sort()        # Sort list
    # Calculate median
    iPos = int((iLen - 1) / 2)
    print(iList)        # Check what the list looks like
    # If list length is odd
    if iLen % 2 != 0:
        print(f"Median: {iList[iPos]}")
    # If list length is even
    else:
        iMedian = (iList[iPos] + iList[iPos + 1]) / 2
        print(f"Median: {iMedian}")
median()


