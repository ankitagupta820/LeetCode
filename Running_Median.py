"""
input: a is array of numbers, to be read one at a time.
output: return array of length n with all medians calculated at every addition of new item.
"""


from heapq import *
def runningMedian(a):

    under = []
    upper = []
    result = []
    N = len(a)
    for i in a:
        curNumber = i
        if (len(upper) == 0):
            upper.append(curNumber)
            result.append(curNumber)
            continue
        middle = upper[0]
        if curNumber >= middle:
            heappush(upper,curNumber)
        else:
            heappush(under, -curNumber)
        if len(under) >= len(upper):
            heappush(upper, -heappop(under))
        if len(upper) >= len(under) + 2:
            heappush(under, -heappop(upper))
        if (len(upper) + len(under)) % 2 == 1:
            result.append(float(upper[0]))
        else:
            result.append((float(upper[0]) + -under[0])/2)
    return result
    
