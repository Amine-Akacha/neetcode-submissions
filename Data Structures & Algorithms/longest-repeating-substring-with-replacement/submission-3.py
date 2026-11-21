class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        size = 0
        store = {}
        for r in range(len(s)):
            cur = s[r]
            store[cur] = store.get(cur,0) +1

            maxValue = max(store.values())

            arrLen = r +1 - l

            if arrLen > maxValue + k:
                cur = s[l]
                store[cur] -= 1
                l += 1
            size = max(size, r +1 - l)

            #print(maxValue)
        return size




        


        

        