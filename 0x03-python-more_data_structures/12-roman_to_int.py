#!/usr/bin/python3
def roman_to_int(roman_string):
    romValue = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    intVal = 0
    rome = roman_string
    if type(roman_string) != str or roman_string is None:
        return None
    for i in range(len(roman_string)):
        if i > 0 and romValue[rome[i]] > romValue[rome[i - 1]]:
            intVal += romValue[rome[i - 1]] - 2 * romValue[rome[i - 1]]
        else:
            intVal += romValue[rome[i]]
    return intVal