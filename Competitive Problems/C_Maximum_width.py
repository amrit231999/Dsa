from collections import defaultdict
n,m=map(int,input().split())
s=str(input())
t=str(input())
mp=defaultdict(list)
freq=defaultdict(int)
cur_freq_s=defaultdict(int)
cur_freq_t=defaultdict(int)
for i in range(len(s)):
    mp[s[i]].append(i)
ans=-1
for i in range(len(t)):
    freq[t[i]]+=1
cur_freq_t[t[0]]+=1
for i in range(1,len(t)):
    max_cur=mp[t[i]][len(mp[t[i]])-(freq[t[i]]-cur_freq_t[t[i]])]
    min_prev=mp[t[i-1]][cur_freq_t[t[i-1]]-1]
    cur_freq_t[t[i]]+=1
    ans=max(ans,max_cur-min_prev)
print(ans)
