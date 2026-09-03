class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1
        n = nums
        l = 0
        r = len(n) - 1
        t = target
        while l <= r:
            m = (r+l) // 2
            if n[l] == t:
                return l
            if n[l] <= n[r]: # sorted array.
                if n[m] > t:
                    r = m - 1
                elif n[m] < t:
                    l = m + 1
                else:
                    return m
            elif n[l] > n[r]: # left bigger than right
                if t > n[l]: # target bigger than left
                    if n[m] >= n[l]:
                        if t > n[m]:
                            l = m + 1
                        elif t < n[m]:
                            r = m - 1
                        else:
                            return m
                    elif n[m] < n[l]:
                        r = m   # move right to middle
                elif t < n[l]: # target smaller than left
                    if n[m] >= n[l]: # left to middle is sorted
                        l = m + 1   # check the right side, left side is bigger
                    elif n[m] < n[l]: # left to middle is unsorted - middle to right is sorted
                        if t < n[m]: # target is smaller than middle
                            r = m - 1 # middle to right is already sorted, so move left
                        elif t > n[m]: #target is bigger than middle but still smaller than left
                            l = m + 1 # check the right side
                        else:
                            return m # middle matches
                else:
                    return l
        return -1


# [5,1,2,3,4] t = 1
# 1- l = 0(5), m = 2(2), r = 4(4)
# 2- l=0, m = 0, r = 1

