class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        n = nums
        t = target
        r = len(n) - 1

        while l <= r:
            m = (l + r) // 2 
            if t == n[m]:
                return m
            if n[l] <= n[r]:
                if n[m] > t:
                    r = m - 1
                elif n[m] < t:
                    l = m + 1
                else:
                    return m
            elif n[l] > n[r]:
                if n[m] >= n[l]:  # l to m sorted
                    if t >= n[l] and t <= n[m]:
                        r = m
                    else:
                        l = m + 1
                else:
                    if t >= n[m] and t <= n[r]:
                        l = m
                    else:
                        r = m - 1

            
        return -1