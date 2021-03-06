#Find the Running Median
#The median of a set of integers is the midpoint value of the data set for which an equal number of integers are less than and greater than the value. To find the median, you must first sort your set of integers in non-decreasing order, then:
#
#If your set contains an odd number of elements, the median is the middle element of the sorted sample. In the sorted set ,  is the median.
#If your set contains an even number of elements, the median is the average of the two middle elements of the sorted sample. In the sorted set ,  is the median.
#Given an input stream of  integers, you must perform the following task for each  integer:
#
#Add the  integer to a running list of integers.
#Find the median of the updated list (i.e., for the first element through the  element).
#Print the list's updated median on a new line. The printed value must be a double-precision number scaled to  decimal place (i.e.,  format).


#!/bin/python3

import os
import sys
import bisect

#
# Complete the runningMedian function below.
#
def runningMedian(a,fptr):
    #a.sort()
    mid=(len(a)/2)-1
    #print(round(mid)," ",len(a))
    if(len(a)%2==0):
        median=(a[int(mid)]+a[int(mid)+1])/2
    else:
        median=a[int(mid+0.5)]
    
    fptr.write('%.1f'%median)
    fptr.write('\n')


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = []

    for _ in range(a_count):
        a_item = int(input())
        bisect.insort(a,a_item)
        runningMedian(a,fptr)


    #result = 
    #fptr.write('\n'.join(map(str, result)))
    #fptr.write('\n')

    fptr.close()
