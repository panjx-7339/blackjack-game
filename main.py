import random
import os
from art import logo


def cls():
    """
    clears the console in macOS.
    """
    # os.environ['TERM'] = 'xterm-color'
    os.system('cls' if os.name == 'nt' else 'clear')


def deal_cards(hand, n):
    """
    deals a random n number of cards and updates the computer's or player's hand/
    """
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    for i in range(n):
        hand.append(random.choice(deck))
    return hand


def print_scores(p_hand, d_hand):
    """
    takes the player's and dealer's hand and returns current game scores,
    while the game has not ended.
    """
    print(f"\tYour cards: {p_hand}, current score: {sum(p_hand)}")
    print(f"\tDealer's first card: {d_hand[0]}")
    print()


def print_result(p_hand, d_hand):
    """
    takes the player's and dealer's hands and returns their final hand and scores.
    """
    print(f"\tYour final hand: {p_hand}, final score: {sum(p_hand)}")
    print(f"\tDealer's final hand: {d_hand}, final score: {sum(d_hand)}")
    print()


def start_game():
    """
    asks the user if they wish to start a new game.
    If the user says yes, this function clears the console and starts the game.
    """
    start_game = input("Do you wish to play a game of Blackjack? Type 'y' or 'n': ")
    if start_game == 'y':
        cls()
        play_game()
    else:
        print("Goodbye")


def calculate_score(hand):
    """
    Returns the sum of the cards in the player's or dealer's hand
    """
    score = sum(hand)
    if score == 21 and len(hand) == 2:
        return 0
    elif (11 in hand) and score > 21:  # an ace is counted as 1, instead of 11, if the score exceeds 21
        hand.remove(11)
        hand.append(1)
    return sum(hand)


def compare(p_score, d_score):
    """
    compares player's and dealer's scores and returns the game result
    """
    if p_score > 21:
        return "You went over. You lose 😭"
    elif d_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif p_score == 0:
        return "Win with a Blackjack 😎"
    elif p_score == d_score:
        return "Draw 🙃"
    elif d_score > 21:
        return "Opponent went over. You win 😁"
    elif p_score > d_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo)

    p_hand, d_hand = [], []  # players each start off with an empty hand
    is_game_over = False

    # deal two random cards each to the player and dealer
    p_hand = deal_cards(p_hand, 2)
    d_hand = deal_cards(d_hand, 2)

    while not is_game_over:     # while game is not over, or player is still drawing cards
        p_score = calculate_score(p_hand)
        d_score = calculate_score(d_hand)
        print_scores(p_hand, d_hand)

        if p_score == 0 or d_score == 0 or p_score > 21:
            is_game_over = True
        else:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if another_card == 'y':
                p_hand = deal_cards(p_hand, 1)
            else:
                is_game_over = True

    # User stops playing
    # The dealer draws cards until it gets a blackjack or their score is more than 17
    while d_score != 0 and d_score < 17:
        d_hand = deal_cards(d_hand, 1)
        d_score = calculate_score(d_hand)

    # Game ends and results are shown
    print_result(p_hand, d_hand)
    print(compare(p_score, d_score))

    start_game()


start_game()
