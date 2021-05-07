import sys
import math
input = sys.stdin.readline


def check(x):
    z = int(math.sqrt(x//2))
    if z*z == x//2 and x % 2 == 0:
        return 1
    z = int(math.sqrt(x//4))
    if z*z == x//4 and x % 4 == 0:
        return 1
    return 0


for _ in range(int(input())):
    n = int(input())
    print(["NO", "YES"][check(n)])
