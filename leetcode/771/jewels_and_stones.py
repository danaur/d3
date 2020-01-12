class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = set()

        for jewel in J:
            jewels.add(jewel)

        jewel_count = 0
        for stone in S:
            if stone in jewels:
                jewel_count += 1

        return jewel_count
