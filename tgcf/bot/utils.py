from typing import List

from tgcf.config import Forward


def get_args(text: str):
    splitted = text.split(" ", 1)
    if not len(splitted) == 2:
        return ""
    else:
        prefix, args = splitted
    print(prefix)
    args = args.strip()
    print(args)
    return args


def display_forwards(forwards: List[Forward]):
    if len(forwards) == 0:
        return "Currently no forwards are set"
    forward_str = "This is your configuration"
    for forward in forwards:
        forward_str = (
            forward_str
            + f"\n\n```\nsource: {forward.source}\ndest: {forward.dest}\n```\n------------"
        )

    return forward_str


def remove_source(source, forwards: List[Forward]):
    for i, forward in enumerate(forwards):
        print(forward)
        print(type(forward.source))
        print(type(source))
        if forward.source == source:

            del forwards[i]

            return forwards

    else:
        raise ValueError("The source does not exist")
