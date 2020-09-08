#2D Array - DS

#!/bin/python3

import math
import os as os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sum=-9999
    for i in range(0,4):
        for j in range(0,4):
            new_sum=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            if(new_sum>sum):
                print(new_sum)
                sum=new_sum
    return sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
