class Solution(object):
    def decodeString(self, s):
        stack = []  # To store previous strings and their multipliers
        num = 0  # To store the current number
        temp = ""  # To store the current decoded string

        for i in s:
            if i.isdigit():  # to handle multi-digit numbers
                num = (num * 10) + int(i)

            elif i == '[':  # Push the current string and multiplier onto the stack
                stack.append((temp, num))
                # Reset num and temp for the next segment
                num = 0  
                temp = ""  

            elif i == ']':  # Pop from stack to decode the substring
                string, nums = stack.pop()
                temp = string + (temp * nums)  # Repeat the substring and concatenate

            else:  # Append alphabets to the current string
                temp += i

        return temp

        