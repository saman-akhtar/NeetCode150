class Solution:
    def calculate(self, s: str) -> int:
        prev = 0
        cur = 0
        res = 0
        cur_op = "+"
        i =0
        while i < len(s):
            ch = s[i]
            if ch.isdigit():
                while i < len(s) and s[i].isdigit():
                    cur = cur * 10 + int(s[i])
                    i += 1
                i -=1
                ch = s[i]
                if cur_op == "+":
                    res += cur
                    prev = cur

                elif cur_op == "-":
                    res -= cur
                    prev = -cur
                elif cur_op == "*":
                    res -= prev
                    res += prev * cur

                    prev = prev * cur
                elif cur_op == "/":
                    res -= prev
                    res += int(prev / cur)

                    prev = int(prev / cur)
                cur = 0
            elif ch != " ":
                cur_op = ch
            i +=1
        return res