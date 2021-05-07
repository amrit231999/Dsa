import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, x = map(int, input().split())
    v = list(map(int, input().split()))
    sum = 0
    pos = -1
    flag = 0
    for i in range(n):
        sum += v[i]
        if sum == x and i == n-1:
            flag = 1

        elif sum == x:
            pos = i

    if flag:
        print("NO")
    else:
        print("YES")
        if pos == -1:
            print(*v)
        else:
            for i in range(pos):
                print(v[i], end=" ")

            print(v[pos+1], end=" ")
            print(v[pos], end=" ")

            for i in range(pos+2, n):
                print(v[i], end=" ")

            print("")
