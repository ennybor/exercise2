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
        pass

    def get_numerator(self):
        #TODO
        pass

    def get_denominator(self):
        #TODO
        pass

    def get_fraction(self):
        #TODO
        pass