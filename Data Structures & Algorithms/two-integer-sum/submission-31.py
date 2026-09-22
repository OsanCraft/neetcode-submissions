class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, n in enumerate(nums):
            cp = target - n
            if cp in seen:
                return [seen[cp], i]
            seen[n] = i

        