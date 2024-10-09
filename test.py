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




