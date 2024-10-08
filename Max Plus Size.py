#link: https://codeforces.com/contest/2019/problem/A?csrf_token=f5804d2aa5cec9412a6a62dd0b885716
import math
for _ in range(int(input())):       #even faster version
    n = int(input())
    a = [int(x) for x in input().split()]
    a.insert(0,-1)
    ans=-1
    if(n%2==0):
        ans = max(a)+math.ceil(n/2)
    else:
        if(a.index(max(a))%2!=0):
            ans = max(a) + math.ceil(n/2)
        else:
            ans = max(a) + math.ceil(n/2)-1
    print(int(ans))