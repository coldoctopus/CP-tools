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
    
#chatgpt version
key = []
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    total_cards = sum(a)  # Total number of cards you have
    a.sort(reverse=True)  # Sort the card types by how many you have, in descending order
    
    max_deck_size = 0
    
    # We will iterate over all possible deck sizes from 1 to n
    for deck_size in range(1, n+1):
        # Calculate how many full decks of this size we can form
        full_decks = 0
        needed_cards = 0  # Cards we need to complete more decks
        
        for cards_of_type in a:
            if cards_of_type >= deck_size:
                full_decks += cards_of_type // deck_size
            else:
                needed_cards += (deck_size - cards_of_type)
        
        # If the number of needed cards is less than or equal to the cards we can buy, this deck size is valid
        if needed_cards <= k:
            max_deck_size = max(max_deck_size, deck_size)
    
    key.append(max_deck_size)

for ans in key:
    print(ans)
    



