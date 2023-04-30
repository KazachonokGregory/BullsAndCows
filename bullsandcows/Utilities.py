class Number:
    def __init__(self, number):
        self.digits = []

        while number > 0:
            self.digits.append(number % 10)
            number //= 10
        self.digits.reverse()

    def __getitem__(self, index):
        return self.digits[index]

    def __eq__(self, other):
        return self.digits == other.digits

    def __ne__(self, other):
        return self.digits != other.digits

    def as_string(self):
        result = ""
        for digit in self.digits:
            result += str(digit)

    def is_valid(self):
        if len(self.digits) != 4:
            return False
        for digit in self.digits:
            if self.digits.count(digit) > 1:
                return False
        return True


# all_numbers = [Number(number) for number in range(1, 10000) if Number(number).is_valid()]

def get_bulls(first, second):
    bulls = 0
    for first_digit, second_digit in zip(first, second):
        if first_digit == second_digit:
            bulls += 1
    return bulls

def get_cows(first, second):
    cows = 0
    for digit in first:
        if digit in second:
            cows += 1
    return cows
