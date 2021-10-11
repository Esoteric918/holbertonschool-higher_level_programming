#!/usr/bin/python
""" Prints 2 new lines after ., ? and : """


def text_indentation(text):
    """ determins if text is str or not and print new lines"""

    if type(text) != str:
        raise TypeError("text must be a string")
    for i in text:
        if i == '.' or i == '?' or i == ":":
            print("{} {}".format(i, '\n'))
        else:
            print(i, end="")
