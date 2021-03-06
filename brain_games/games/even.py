"""Brain-even game resources."""

import random

from brain_games import engine

INSTRUCTIONS = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_round():
    """Сreate a question and answer for one stage of game.

    Returns:
        tuple: Question and correct answer for current round.
    """
    question = random.randint(1, 100)
    correct_answer = 'yes' if question % 2 == 0 else 'no'

    return question, correct_answer


def play():
    """Start the game."""
    engine.play(INSTRUCTIONS, get_round)
