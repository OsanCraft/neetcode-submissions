class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases: 1 way for 1 step, 2 ways for 2 steps
        if n <= 2:
            return n
        
        # prev is step 1 (1 way), curr is step 2 (2 ways)
        prev, curr = 1, 2
        
        # Iteratively calculate ways for steps 3 up to n
        for _ in range(3, n + 1):
            prev, curr = curr, prev + curr
        
        return curr
