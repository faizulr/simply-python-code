"""Tests for the sum_game module."""

import itertools

import pytest

import sum_game


def test_generate_question_invalid_range():
    """generate_question should guard against an invalid range."""
    with pytest.raises(ValueError):
        sum_game.generate_question(min_value=5, max_value=4)


def test_play_math_game_flow(monkeypatch):
    """The game should prompt, validate input, and report outcomes each round."""
    numbers = itertools.cycle([1, 2, 4, 5])
    monkeypatch.setattr(sum_game.random, "randint", lambda *_: next(numbers))

    responses = iter(["abc", "3", "10"])
    captured_output = []

    def fake_input(prompt: str) -> str:
        captured_output.append(prompt)
        return next(responses)

    def fake_print(message: str) -> None:
        captured_output.append(message)

    sum_game.play_math_game(rounds=2, input_fn=fake_input, print_fn=fake_print)

    assert captured_output == [
        "Round 1: What is 1 + 2? ",
        "Please enter a valid integer.",
        "Round 1: What is 1 + 2? ",
        "Correct!",
        "Round 2: What is 4 + 5? ",
        "Incorrect. The correct answer was 9.",
        "Thanks for playing!",
    ]


def test_play_math_game_invalid_rounds():
    """A non-positive round count should raise a ValueError."""
    with pytest.raises(ValueError):
        sum_game.play_math_game(rounds=0)
