class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        #loop through nums
        # replace nums[val] with None
        #return the new list and the count

        i = 0

        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i

        