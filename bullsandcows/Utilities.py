DIGIT_COUNT = 4

def is_almost_valid(number):
    if number == "":
        return True
    if number[0] == '0':
        return False
    if not number.isdigit() or len(number) > DIGIT_COUNT:
        return False
    for digit in number:
        if number.count(digit) > 1:
            return False
    return True

def is_valid(number):
    return is_almost_valid(number) and len(number) == DIGIT_COUNT

def get_bulls(first, second):
    bulls = 0
    for first_digit, second_digit in zip(first, second):
        if first_digit == second_digit:
            bulls += 1
    return bulls

def get_cows(first, second):
    cows = 0
    for first_digit, second_digit in zip(first, second):
        if first_digit != second_digit and first_digit in second:
            cows += 1
    return cows
