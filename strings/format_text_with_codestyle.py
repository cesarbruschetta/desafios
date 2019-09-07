""" """
import sys
import argparse
from textwrap import wrap


def left_justify(words, width):
    """Given an iterable of words, return a string consisting of the words
    left-justified in a line of the given width.

    >>> left_justify(["hello", "world"], 16)
    'hello world     '

    """
    return " ".join(words).ljust(width)


def justify(words, width):
    """Divide words (an iterable of strings) into lines of the given
    width, and generate them. The lines are fully justified, except
    for the last line, and lines with a single word, which are
    left-justified.

    >>> words = "This is an example of text justification.".split()
    >>> list(justify(words, 16))
    ['This    is    an', 'example  of text', 'justification.  ']

    """
    line = []  # List of words in current line.
    col = 0  # Starting column of next word added to line.
    for word in words:
        if line and col + len(word) > width:
            if len(line) == 1:
                yield left_justify(line, width)
            else:
                # After n + 1 spaces are placed between each pair of
                # words, there are r spaces left over; these result in
                # wider spaces at the left.
                n, r = divmod(width - col + 1, len(line) - 1)
                narrow = " " * (n + 1)
                if r == 0:
                    yield narrow.join(line)
                else:
                    wide = " " * (n + 2)
                    yield wide.join(line[:r] + [narrow.join(line[r:])])
            line, col = [], 0
        line.append(word)
        col += len(word) + 1
    if line:
        yield left_justify(line, width)


def main_parser(sargs):

    parser = argparse.ArgumentParser(
        description="Script para formatar texto com o padrão do coding style do kernel Linux"
    )

    parser.add_argument(
        "--size", default=40, type=int, help="Quantidade de caracteres por linha"
    )
    parser.add_argument(
        "--justificar",
        action="store_true",
        default=False,
        help="Retorna o arquivo formatado e justificado",
    )

    parser.add_argument("text", help="Texto a ser formatado")

    ################################################################################################
    args = parser.parse_args(sargs)
    SPACE = args.size

    if args.justificar:

        words = args.text.split()
        print("\n".join(justify(words, args.size)))

    else:
        print("\n", "#" * SPACE, "Texto formataro", "#" * SPACE)
        print("\n".join(["\n".join(wrap(args.text, width=args.size))]))

    return 0


if __name__ == "__main__":
    sys.exit(main_parser(sys.argv[1:]))
