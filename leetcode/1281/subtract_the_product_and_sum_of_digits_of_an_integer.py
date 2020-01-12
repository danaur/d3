#!/usr/bin/python3

import functools

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # Intentionally avoiding marshalling to string and back
        digits = []

        while n > 0:
            last_digit = n % 10;
            digits.append(last_digit)
            n //= 10

        multiplcation_result = functools.reduce(lambda a, b: a*b, digits)
        sum_result = sum(digits)

        return multiplcation_result - sum_result




