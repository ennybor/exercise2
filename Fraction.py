class Fraction(object):
    def __init__(self, numerator=0, denominator=1):
        if isinstance(numerator, str):
            fraction_string = numerator.strip()
            if fraction_string.count("/") > 1:
                self.numerator = 0
                self.denominator = 1
            elif '/' in fraction_string:
                num, denom = fraction_string.split('/')
                if num.isdigit() and denom.isdigit:
                    self.numerator = int(num)
                    self.denominator = int(denom)
                else:
                    self.numerator = 0
                    self.denominator = 1
            elif fraction_string.isdigit():
                self.numerator = int(fraction_string)
                self.denominator = 1
            else:
                self.numerator = 0
                self.denominator = 1
        elif isinstance(numerator, int):
            if denominator == 0:
                raise ZeroDivisionError("Denominator cannot be zero")
            self.numerator = numerator
            self.denominator = denominator
        elif isinstance(numerator, float):
            self.numerator = 0
            self.denominator = 1
        else:
            raise ValueError("Invalid input type")

    @staticmethod
    def gcd(a, b):
        """Return the greatest common divisor of a and b using the Euclidean algorithm."""
        if a == 0 or b == 0:
            return 0
        while b:
            a, b = b, a % b
        return a

    def get_numerator(self):
        """Return the numerator as a string."""
        return str(self.numerator)

    def get_denominator(self):
        """Return the denominator as a string."""
        return str(self.denominator)

    def get_fraction(self):
        """Return the fraction as a string in the form 'numerator/denominator' or just 'numerator'."""
        gcd = self.gcd(self.numerator, self.denominator)
        if self.denominator == 1:
            return str(self.numerator)
        elif gcd > 1 or gcd < -1:
            self.numerator = int(self.numerator / gcd)
            self.denominator = int(self.denominator / gcd)
            return f"{self.numerator}/{self.denominator}"
        else:
            return f"{self.numerator}/{self.denominator}"