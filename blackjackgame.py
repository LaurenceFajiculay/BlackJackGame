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

    # Check if player has busted
    if player_score > 21:
        print("Player busted!")
        break

    # Ask player if they want to hit or stand
    action = input("Do you want to hit or stand? ")

    # If player stands, break out of the loop
    if action.lower() == "stand":
        break

    # If player hits, deal another card
    player_cards.append(cards.pop()) 

    # Dealer's turn
while True:
    # Calculate dealer's total score
    dealer_score = sum(dealer_cards)

    # Show dealer's cards and score
    print("Dealer's cards:")
    for card in dealer_cards:
        print(card)
    print(f"Dealer's score: {dealer_score}")

    # Check if dealer has busted
    if dealer_score > 21:
        print("Dealer busted!")
        break

    # If dealer has less than 17 points, hit
    if dealer_score < 17:
        dealer_cards.append(cards.pop())
    else:
        # Stand if dealer has 17 or more points
        print("Dealer stands.")
        break

