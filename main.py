key = []
for _ in range(int(input())):   
    n, k= map(int, input().split())   
    a = input().split()
    a = [int(x) for x in a]
    deck = max(a)
    card = sum(a)
    ans = -1
    while(ans==-1):
        koin = k
        while(koin>=0):
            if((card+koin)%deck!=0):
                koin-=1
            else:
                ans = (card+koin)/deck
        deck+=1
        
    
    # for i in range(sum(a),k,1):
    #     if ((sum(a)+i)%n==0):
    #         ans = max(ans,(sum(a)+i)/n)
    key.append(ans)

print(key)