class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        #TODO
        if isinstance(numerator, str):
            fraction_string = numerator.strip()
            if '/' in fraction_string:
                num, denom = fraction_string.split('/')
                self.numerator = int(num)
                self.denominator = int(denom)
            else:
                self.numerator = int(fraction_string)
                self.denominator = 1
        elif isinstance(numerator, int):
            if denominator == 0:
                raise ZeroDivisionError("Denominator cannot be zero")
            self.numerator = numerator
            self.denominator = denominator
        else:
            raise ValueError("Invalid input type")

    def gcd(a, b):
        #TODO
        if a == 0 and b == 0:
            return 0
        while b:
            a, b = b, a % b
        return a

    def get_numerator(self):
        #TODO
        return str(self.numerator)

    def get_denominator(self):
        #TODO
        return str(self.denominator)

    def get_fraction(self):
        #TODO
        if self.denominator == 1:
            return str(self.numerator)
        else:
            return f"{self.numerator}/{self.denominator}"