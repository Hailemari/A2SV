import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    prefixSum = [0] * (n + 1)
    
    # Perform operations and update the prefix sum array
    for query in queries:
        a, b, k = query
        prefixSum[a-1] += k
        prefixSum[b] -= k
    maxValue = 0
    s = 0
    
    # Calculate the actual array  based on the prefix sum array
    for i in range(n):
        s += prefixSum[i]
        maxValue = max(maxValue, s)
        
    return maxValue
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
