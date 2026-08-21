
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        bestSpeed = r
        while l <= r:
            m = (r + l) // 2
            totalH = 0
            for i in piles:
                eatSpeed = -(i // -m)
                totalH += eatSpeed
            if totalH <= h:
                r = m - 1
                bestSpeed = min(bestSpeed, m)
            else:
                l = m + 1
        return bestSpeed

