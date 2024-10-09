# link: https://codeforces.com/contest/2009/problem/E
import math as m
def partialSum(l,r):
    return (r*(r+1)/2) - (l*(l-1)/2)
    
for _ in range(int(input())):       #even faster version
    n,k = map(int, input().split()) 
    left = k
    right = k+n-1
    ans = pow(10,9)
    
    while left<=right:
        mid = m.ceil((left+right)/2)
        m1 = m.ceil(partialSum(k,mid))
        m2 = m.ceil(partialSum(mid+1,k+n-1))
        ans = min(ans, abs(m1-m2))
        if(m1>m2):
            right = mid-1
        else:
            left = mid+1
    
    print(ans)
    
    
    



