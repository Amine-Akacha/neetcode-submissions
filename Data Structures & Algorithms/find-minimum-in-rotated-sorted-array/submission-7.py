class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        n = nums
        m = 0
        while l < r:
            m = (l+r) // 2
            if n[l] > n[m]:
                if n[l] > n[r] and n[m] > n[r]:
                    l = m
                else:
                    r = m
            elif n[l] <= n[m]:
                if n[l] > n[r]:
                    l = m + 1
                else:
                    r = m
        return n[l]


            # [3,4,5,1,2] 
            # [1,2,3,4,5]
            # [4,5,0,1,2,3]
            # 