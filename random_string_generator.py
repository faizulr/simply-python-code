"""Generate random strings with configurable length and character options."""

import argparse
import secrets
import string
from typing import Iterable

DEFAULT_CHARSET = string.ascii_letters + string.digits


def build_charset(
    *,
    use_lowercase: bool = True,
    use_uppercase: bool = True,
    use_digits: bool = True,
    use_punctuation: bool = False,
    extra_characters: Iterable[str] | None = None,
) -> str:
    """Create a character set string based on provided options."""

    charset_parts = []
    if use_lowercase:
        charset_parts.append(string.ascii_lowercase)
    if use_uppercase:
        charset_parts.append(string.ascii_uppercase)
    if use_digits:
        charset_parts.append(string.digits)
    if use_punctuation:
        charset_parts.append(string.punctuation)
    if extra_characters:
        charset_parts.append("".join(extra_characters))

    charset = "".join(charset_parts)
    if not charset:
        raise ValueError("At least one character option must be selected to build a charset.")

    return charset


def generate_random_string(length: int = 100, charset: str = DEFAULT_CHARSET) -> str:
    """Generate a random string.

    Args:
        length: Desired length of the string. Must be a positive integer.
        charset: Characters to sample from. Must be non-empty.

    Returns:
        A randomly generated string of the requested length.

    Raises:
        ValueError: If ``length`` is not positive or ``charset`` is empty.
    """

    if length <= 0:
        raise ValueError("length must be a positive integer")
    if not charset:
        raise ValueError("charset must not be empty")

    return "".join(secrets.choice(charset) for _ in range(length))


def main():
    parser = argparse.ArgumentParser(description="Generate a random string of specified length.")
    parser.add_argument(
        "-l",
        "--length",
        type=int,
        default=100,
        help="Length of the random string to generate (default: 100)",
    )
    parser.add_argument(
        "-c",
        "--charset",
        default=None,
        help=(
            "Custom character set to sample from. Overrides other character selection options if provided."
        ),
    )
    parser.add_argument(
        "--no-lowercase",
        action="store_true",
        help="Exclude lowercase letters from the generated string.",
    )
    parser.add_argument(
        "--no-uppercase",
        action="store_true",
        help="Exclude uppercase letters from the generated string.",
    )
    parser.add_argument(
        "--no-digits",
        action="store_true",
        help="Exclude digits from the generated string.",
    )
    parser.add_argument(
        "--punctuation",
        action="store_true",
        help="Include punctuation characters in the generated string.",
    )

    args = parser.parse_args()

    charset = (
        args.charset
        if args.charset is not None
        else build_charset(
            use_lowercase=not args.no_lowercase,
            use_uppercase=not args.no_uppercase,
            use_digits=not args.no_digits,
            use_punctuation=args.punctuation,
        )
    )

    random_string = generate_random_string(args.length, charset)
    print(random_string)


if __name__ == "__main__":
    main()
