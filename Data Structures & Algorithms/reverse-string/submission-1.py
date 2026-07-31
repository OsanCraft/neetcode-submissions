class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # have 2 pointers go from the last and 2nd last item,
        #append them on a seperate list
        #after sorting, replace s with that placeholder list

        stack = []

        for c in s:
            stack.append(c)
        
        i = 0
        
        while stack:
            s[i] = stack.pop()
            i += 1

        





