import random

# Create a list of cards
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Shuffle the cards
random.shuffle(cards)

# Dealer and player cards
dealer_cards = []
player_cards = []

# Deal initial cards
player_cards.append(cards.pop())
dealer_cards.append(cards.pop())

# Player's turn
while True:
    # Calculate player's total score
    player_score = sum(player_cards)

    # Show player's cards and score
    print("Player's cards:")
    for card in player_cards:
        print(card)
    print(f"Player's score: {player_score}")
