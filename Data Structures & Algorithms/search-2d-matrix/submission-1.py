class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        lenA = len(matrix[0])
        lenM = len(matrix)
        l = 0
        r = lenA * lenM - 1

        while l <= r:
            x = (r + l) // 2
            mL = x // lenA
            mR = x % lenA
            m = matrix[mL][mR]
            print(m)
            if m > target:
                r = x - 1
            elif m < target:
                l = x+1
            else:
                return True
        return False

        # 11 = m[2][3] 
        # 4 = m[1][0]