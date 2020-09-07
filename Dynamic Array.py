#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, que):
    # Write your code here
    seq=[ [] for _ in range( n ) ]
    
    #print(seq)
    output=[]
    lastans=0
    for i in range(len(que)):
        if(que[i][0]==1):
            seq_no=((que[i][1] ^ lastans)%n)
            seq[seq_no].append(que[i][2])
            #print("appended ",seq_no,seq)
        else:
            seq_no=((que[i][1] ^ lastans)%n)
            print(seq_no)
            try:
                lastans=seq[seq_no][que[i][2] % len(seq[seq_no])]
                output.append(lastans)
            except:
                pass
            #print("extracted ",lastans)
    return output



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
