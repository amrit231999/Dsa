s=str(input())
for i in range(len(s)):
    if i%2==0:
        if s[i]<'a' or s[i]>'z':
            print("No")
            exit(0)
    else:
        if s[i]<'A' or s[i]>'Z':
            print("No")
            exit(0)
print("Yes")