import random
import logo
print(logo.logo)
def card_picker():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    score = sum(cards)
    if score == 21 and len(cards) == 2:
        return 0  # Blackjack
    while 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score

def compare(u_score, c_score):
    if u_score == c_score:
        return "Match draw"
    elif u_score == 0:
        return "Win with a Blackjack!"
    elif c_score == 0:
        return "Loss, opponent has a Blackjack!"
    elif u_score > 21:
        return "Loss, you busted!"
    elif c_score > 21:
        return "Win, opponent busted!"
    elif u_score > c_score:
        return "Win"
    else:
        return "Loss"

def play_again():
    user_cards = []
    computer_cards = []
    
    for _ in range(2):
        user_cards.append(card_picker())
        computer_cards.append(card_picker())
    
    is_game_over = False
    
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        print(f"User cards: {user_cards}, User score: {user_score}")
        print(f"Computer cards: [{computer_cards[0]}, ?]")
        
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Do you want to draw another card? (y/n): ").strip().lower()
            if user_should_deal == "y":
                user_cards.append(card_picker())
            else:
                is_game_over = True
    
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(card_picker())
        computer_score = calculate_score(computer_cards)
    
    print(f"User cards: {user_cards}, User score: {user_score}") 
    print(f"Computer cards: {computer_cards}, Computer score: {computer_score}")
    print(compare(user_score, computer_score))

play = input("Do you want to play this game? (y/n): ").strip().lower()
while play == "y":
    # print("\n" * 22)
    play_again()
    play = input("Do you want to play again? (y/n): ").strip().lower()
