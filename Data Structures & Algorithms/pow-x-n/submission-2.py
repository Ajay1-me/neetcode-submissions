class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0

        while n > 0:
            if n % 2 == 1:  # Odd exponent: save one factor of x
                result *= x

            x *= x         # Square the base
            n //= 2        # Halve the exponent

        return result