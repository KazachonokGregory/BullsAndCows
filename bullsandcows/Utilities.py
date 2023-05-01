def is_valid(number):
    if not number.isdigit() or len(number) != 4:
        return False
    for digit in number:
        if number.count(digit) > 1:
            return False
    return True

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
