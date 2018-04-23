class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        last_occurence = {}

        max_length = 0
        start = 0

        for index, char in enumerate(s):
            if char in last_occurence:
                max_length = max(max_length, index - start) # Check if the previous run was longer than the current maximum
                start = max(last_occurence[char] + 1, start) # Advance past last character, ignore if already advanced past that

            last_occurence[char] = index

        max_length = max(max_length, len(s) - start) # Check from the current start to the end

        return max_length


