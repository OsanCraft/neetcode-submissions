class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hashmap
        #loop nums
        seen = {}

        for i in nums:
            if i in seen:
                return True
            seen[i] = i
        return False
        