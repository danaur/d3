class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_digit_count = 0
        for num in nums:
            if self.hasEvenNumberOfDigits(num):
                even_digit_count += 1
        return even_digit_count

    def hasEvenNumberOfDigits(self, num: int):
        # TODO Could probably do a silly optimization here that doesn't count the digits,
        # but not super interested in it right now.
        digit_count = 0
        while num > 0:
            digit_count += 1
            num //= 10
        return digit_count % 2 == 0
