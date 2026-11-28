class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = numbers
        t = target
        l = 0
        r = len(n) - 1

        while l < r:
            tot = n[l] + n[r]

            if tot == t:
                return [l+1, r+1]
            elif tot > t:
                r -= 1
            else:
                l += 1
        