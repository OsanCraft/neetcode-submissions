class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # value: index

        for i, v in enumerate(nums):
            compliment = target - v
            if compliment in seen:
                return [seen[compliment], i]
            seen[v] = i
            
            
        