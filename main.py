
def getMaxPts(a,start):
    max_val = -1
    count_val = 0
    for i in range(start,len(a),2):
        count_val+=1
        max_val = max(a[i],max_val)
    return max_val+count_val

for _ in range(int(input())):       #even faster version
    n = int(input())
    a = [int(x) for x in input().split()]
    even_res = getMaxPts(a,0)
    odd_res = getMaxPts(a,1)
    ans = max(even_res,odd_res)
    print(int(ans))