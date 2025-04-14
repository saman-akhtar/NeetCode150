class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # built adj list
        # if u build in nav way tc N^ 2  * M = wth constrin it wil be TLC
        # SO adj list buld O(n* m ^2)
        if endWord not in wordList:
            return 0
        adj_list = defaultdict(list)
        wordList.append(beginWord)
        for word in  wordList: # N
            for i in range(len(word)): # m
                pattern = word[:i] + '*' + word[i +1:]
                adj_list[pattern].append(word)
        count = 1
        visit = set([beginWord])
        q = deque([beginWord])

        # bfs
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return count
                for j in range(len(word)):
                    # find pattern
                    pattern =  word[:j] + '*' + word[j + 1:]
                    # * o t : hot, dot, lot
                    # h * t : hot, hit

                    # check pattern's neigh from adj_list
                    for neigh in adj_list[pattern]:
                        if neigh not in visit:
                            visit.add(neigh)
                            q.append(neigh)


            count += 1
                
        return 0

        