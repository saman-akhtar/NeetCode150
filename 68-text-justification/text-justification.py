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
                    parts.append(words[i - 1])                           # last word
                    new_line = "".join(parts)
                    # new_line = per_space.join(words[start: i])
                    # new_line = new_line[:len(words[start])] +  (" " * extra_space )+ new_line[len(words[start]):]
                ans.append(new_line)

                # reset
                # i -=1
                start = i
                cur_len = len(words[i])
                # print("I vali after", i,start)

            i += 1
        last_line = " ".join(words[start:])
        last_line += " " * (maxWidth - len(last_line))
        ans.append(last_line)
        return ans



            
        