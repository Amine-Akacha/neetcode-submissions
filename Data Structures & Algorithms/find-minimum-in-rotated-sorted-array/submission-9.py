class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        n = nums
        while l <= r:
            if n[l] <= n[r]:
                return n[l]
            m = (l + r) // 2
            if n[l] > n[m]:
                r = m
            elif n[m] >= n[l]:
                l = m + 1
        return n[l]
            
