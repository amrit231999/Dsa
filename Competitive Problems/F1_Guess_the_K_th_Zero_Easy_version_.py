from collections import defaultdict
import sys
from sys import stdout
input = sys.stdin.readline
n, t = map(int, input().split())
k = int(input())
low = 1
high = n
while low+1 < high:
    mid = (low+high)//2
    print("? 1 "+str(mid))
    print(" ")
    stdout.flush()
    s = str(input())
    z = int(input())
    if z <= mid-k:
        high = mid
    else:
        low = mid+1

if low == high:
    print("! "+str(low))
    print(" ")
    stdout.flush()
    exit(0)

else:
    print("? 1 "+str(low))
    print(" ")
    stdout.flush()
    s = str(input())
    z = int(input())
    if z == low-k:
        print("! "+str(low))
        print(" ")
        stdout.flush()
        exit(0)

    else:
        print("! "+str(high))
        print(" ")
        stdout.flush()
        exit(0)
