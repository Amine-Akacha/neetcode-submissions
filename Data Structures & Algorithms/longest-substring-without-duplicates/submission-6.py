class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = set()
        l = 0
        best = 0

        for r in range(len(s)):
            if s[r] in store:
                while s[r] in store:
                    store.remove(s[l])
                    l += 1
            store.add(s[r])
            best = max(best, r + 1- l)
        return best

            