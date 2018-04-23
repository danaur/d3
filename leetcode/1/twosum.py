class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        previous_numbers = {}

        for index, num in enumerate(nums):
            if target - num in previous_numbers:
                return [previous_numbers[target - num], index]

            previous_numbers[num] = index
