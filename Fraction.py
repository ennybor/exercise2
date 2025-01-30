import re
from math import gcd

class Fraction(object):
    def __init__(self, numerator=0, denominator=1):
        if isinstance(numerator, str):  # Handle string input
            numerator = numerator.strip()
            match = re.match(r"^(-?\d+)/(-?\d+)$", numerator)
            if match:
                numerator, denominator = int(match.group(1)), int(match.group(2))
            else:
                raise ValueError("Invalid fraction format")
        elif isinstance(numerator, int) and isinstance(denominator, int):
            pass  # Keep as is
        else:
            raise TypeError("Invalid input type")

        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero")

        common_divisor = gcd(abs(numerator), abs(denominator))
        numerator, denominator = numerator // common_divisor, denominator // common_divisor

        if denominator < 0:  # Ensure denominator is always positive
            numerator, denominator = -numerator, -denominator

        self._numerator = numerator
        self._denominator = denominator

    def get_numerator(self):
        return str(self._numerator)

    def get_denominator(self):
        return str(self._denominator)

    def get_fraction(self):
        return f"{self._numerator}" if self._denominator == 1 else f"{self._numerator}/{self._denominator}"

    @staticmethod
    def gcd(a, b):
        return gcd(abs(a), abs(b)) if a or b else 0
