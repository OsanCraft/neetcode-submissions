class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # have 2 pointers go from the last and 2nd last item,
        #append them on a seperate list
        #after sorting, replace s with that placeholder list

        l, r = 0 , len(s) - 1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l, r = l+ 1, r - 1
            

        





