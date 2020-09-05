#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, que):
    arr=[0]*n
    
    
    for i in range(len(que)):
        #arr[que[i][0]-1]+=que[i][2]
        try:
            arr[que[i][0]-1]+=que[i][2]
            arr[que[i][1]]-=que[i][2]
        except:
            pass
    
        
    prev=0
    for i in range (len(arr)):
        prev+=arr[i]
        arr[i]=prev

    return max(arr)


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    #fptr.write(str(result) + '\n')
    print(result)

    #fptr.close()
