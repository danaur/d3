class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for index in range(0, len(nums), 2):
            count = nums[index]
            value = nums[index + 1]
            result.extend([value] * count)
        return result
