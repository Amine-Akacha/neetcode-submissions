class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = nums
        l = 0
        r = len(n) - 1


        while l < r:
            if n[l] < n[r]:
                return n[l]
            m = (l+r) // 2
            if n[l] >= n[r]:
                if n[m] <= n[r]:
                    r = m
                else:
                    l= m +1
        return n[l]
        