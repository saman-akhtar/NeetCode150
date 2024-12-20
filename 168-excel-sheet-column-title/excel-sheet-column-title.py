class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber > 0:
            rem = ( columnNumber -1 ) %26
            res += chr(ord('A') + rem)
            columnNumber = (columnNumber -1 ) // 26
        return res[::-1]
        