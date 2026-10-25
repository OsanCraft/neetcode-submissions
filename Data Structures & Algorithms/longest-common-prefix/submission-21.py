from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]        # just a reference, no copy
        end = len(first)       # an integer: how much of `first` is still shared

        for i in range(1, len(strs)):
            s = strs[i]        # just a reference, no copy
            j = 0
            while j < end and j < len(s) and first[j] == s[j]:
                j += 1
            end = j            # shrink the boundary (an integer, not a new string)

        return first[:end]     # one slice, only to build the answer