for _ in range(int(input())):      
    n,m,r,c = map(int, input().split())
    print((m-c) + (n-r)*m + (n-r)*(m-1))