#!/usr/bin/python3
"""Conains the function text_indentation(text)"""


def text_indentation(text):
    """Prints a text with 2 lines after each of these characters: ., ? and :

    Args:
        text(str): string text
    """
    delim = ['.', '?', ':']
    i = 0

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    while i < len(text):
        if text[i] not in delim:
            print(text[i], end="")
            i += 1
        else:
            print(f"{text[i]}\n")
            i = i + 2
