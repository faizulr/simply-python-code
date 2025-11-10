"""Simple math addition game.

The game presents the player with a series of addition problems
using randomly generated numbers. The player has ten attempts
per session. After each answer the game provides immediate feedback
and moves on to the next question.
"""

from __future__ import annotations

import random
from typing import Callable


def generate_question(min_value: int = 0, max_value: int = 20) -> tuple[int, int]:
    """Return two randomly generated integers between the provided bounds."""
    if min_value > max_value:
        raise ValueError("min_value must not be greater than max_value")
    return random.randint(min_value, max_value), random.randint(min_value, max_value)


def play_math_game(
    rounds: int = 10,
    *,
    min_value: int = 0,
    max_value: int = 20,
    input_fn: Callable[[str], str] = input,
    print_fn: Callable[[str], None] = print,
) -> None:
    """Run the math game for a specified number of rounds.

    Parameters
    ----------
    rounds:
        The number of questions the player will be asked. Defaults to ten.
    min_value, max_value:
        Inclusive bounds for the randomly generated operands.
    input_fn:
        Function used to gather user input. Defaults to :func:`input`.
    print_fn:
        Function used for output. Defaults to :func:`print`.
    """

    if rounds <= 0:
        raise ValueError("rounds must be a positive integer")

    for round_number in range(1, rounds + 1):
        first, second = generate_question(min_value=min_value, max_value=max_value)
        correct_answer = first + second

        while True:
            try:
                user_response = input_fn(
                    f"Round {round_number}: What is {first} + {second}? "
                )
                user_answer = int(user_response)
                break
            except ValueError:
                print_fn("Please enter a valid integer.")

        if user_answer == correct_answer:
            print_fn("Correct!")
        else:
            print_fn(f"Incorrect. The correct answer was {correct_answer}.")

    print_fn("Thanks for playing!")


if __name__ == "__main__":
    play_math_game()
