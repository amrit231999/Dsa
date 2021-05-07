import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    ans = 0
    for i in range(1, 10):
        cur = i
        prod = 10
        while cur <= n:
            ans += 1
            cur += prod*i
            prod *= 10

    print(ans)
