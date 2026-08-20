class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        n = nums
        for i in range(len(nums)):
            r = target - n[i]
            if n[i] in s:
                return [s[n[i]], i]
            s[r] = i
        return []

            # 0: 4
            # 1: 3