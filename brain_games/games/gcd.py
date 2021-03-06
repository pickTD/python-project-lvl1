"""Brain-gcd game resources."""

import math
import random

from brain_games import engine

INSTRUCTIONS = 'Find the greatest common divisor of given numbers.'


def get_round():
    """Сreate a question and answer for one stage of game.

    Returns:
        tuple: Question and correct answer for current round.
    """
    number_one = random.randint(1, 100)
    number_two = random.randint(1, 100)
    question = '{0} {1}'.format(number_one, number_two)
    gcd = math.gcd(number_one, number_two)
    correct_answer = str(gcd)

    return question, correct_answer


def play():
    """Start the game."""
    engine.play(INSTRUCTIONS, get_round)
