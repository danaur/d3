class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        shift_index = 0
        for iter_index, list_value in enumerate(nums):
            if list_value != val:
                nums[shift_index] = list_value
                shift_index += 1
        return shift_index
