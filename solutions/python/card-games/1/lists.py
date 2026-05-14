"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    Parameters:
        number (int):  The current round number.

    Returns:
        list: The current round number and the two that follow.
    """
    round = [number, number+1, number+2]
    return round

def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    Parameters:
        rounds_1 (list):  The first rounds played.
        rounds_2 (list): The second group of rounds played.

    Returns:
        list:  All rounds played.
    """
    
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    Parameters:
        rounds  (list): The rounds played.
        number (int): The round number.

    Returns:
        bool: Was the round played?
    """

    return number in rounds


def card_average(hand):
    """Calculate and returns the average card value from the list.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        float: The average value of the cards in the hand.
    """

    average = sum(hand) / len(hand)
    return average

def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Does one of the approximate averages equal the `true average`?
    """

    average = card_average(hand)
    semi_average1 = (hand[0] + hand[-1]) / 2
    semi_average2 = sorted(hand)[len(hand) // 2]
    if (semi_average1 or semi_average2) == average:
        return True
    return False

def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Are the even and odd averages equal?
    """

    odd_cards = hand[1::2]
    even_cards = hand[0::2]

    odd_average = sum(odd_cards) / len(odd_cards)
    even_average = sum(even_cards) / len(even_cards)

    return even_average == odd_average

def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        list: The hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        hand[-1] = hand[-1] * 2
        return hand
    return hand
