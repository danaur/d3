class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """

        numRows + 1 = distance between two of the same column with no interleaved
        rows 0 and numRows never have zigs


        # NOTES
        initial offset + cycle distance * repeatcount
        cycle distance is rowNum + (rowNum-2)
        initial offset for row N is rowNum + (rowNum-2-N)
        """
        ordered_chunks = []

        cycle_size = numRows + numRows - 2

        if numRows == 1:
            return s

        for row in range(numRows):

            main_index = row

            if row == 0 or row == numRows-1:
                zig_index = None
            else:
                zig_index = numRows + (numRows - 2 - row)

            while main_index < len(s) or (zig_index and zig_index < len(s)):

                if main_index < len(s):
                    ordered_chunks.append(s[main_index])

                if (zig_index and zig_index < len(s)):
                    ordered_chunks.append(s[zig_index])

                main_index += cycle_size
                if zig_index:
                    zig_index += cycle_size
        return "".join(ordered_chunks)


