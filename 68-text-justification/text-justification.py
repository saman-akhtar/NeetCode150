class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        i = 0
        n = len(words)
        start = 0
        cur_len = 0
        while i < n:
            cur_wrd = words[i]
            if cur_len == 0:
                
                cur_len = len(cur_wrd)
            else:
                cur_len += len(cur_wrd) + 1   # space len
            if cur_len > maxWidth:
                no_word = i - start 
                only_wrd_len = cur_len - len(cur_wrd) -( no_word )
                spaces_total = maxWidth - only_wrd_len
                
                if no_word == 1:
                     new_line = words[start] + " " * spaces_total 
                else:
                    gaps = max((no_word-1),1)
                    per_space = " " * (spaces_total // gaps)
                    extra_space = spaces_total %  gaps
                    parts = []
                    for idx in range(start, i - 1):
                        parts.append(words[idx])
                        # first `extra` gaps get 1 extra blank
                        parts.append(per_space + (" " if idx - start < extra_space else ""))
                        #“Put one more space in the left-most gaps until you run out.” 
                        # so extra soace shoul be evendsirtubeted
                    parts.append(words[i - 1])                           # last word
                    new_line = "".join(parts)
                ans.append(new_line)

                # reset
                # i -=1
                start = i
                cur_len = len(words[i])

            i += 1
        last_line = " ".join(words[start:])
        last_line += " " * (maxWidth - len(last_line))
        ans.append(last_line)
        return ans
# Time complexity
# The algorithm does two things:

# Linear pass over the word list
# Each word is examined once and we add len(word) to a running total.
# → cost ≈ Σ len(word) = n · m

# Build each output line once
# When a line is full we “print” it: concatenate all its words and spaces.
# Every word-character is copied exactly once into some output string.
# → additional cost ≈ n · m

# Add them together and constants vanish:

# TC 
# =
# \U0001d442
# (
# \U0001d45b
# ⋅
# \U0001d45a
# )
# TC =O(n⋅m)
# ​
 
# Space complexity
# Required output: the justified text itself is the same size as the input (n · m characters).
# → O(n · m)

# Extra working memory: a handful of integers plus a temporary list that, at most, holds the words that fit on one line (≤ maxWidth, a constant bound).
# → O(maxWidth) ≈ O(1) if maxWidth is treated as fixed.

# SC 
# =
# \U0001d442
# (
# \U0001d45b
# ⋅
# \U0001d45a
# )
#  (output)
# +
# \U0001d442
# (
# 1
# )
#  auxiliary
# SC =O(n⋅m) (output)+O(1) auxiliary
# ​
 


            
        