class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # people.sort(reverse = True)
        # # for i in range(len(people)):
        # i = 0
        # count = 0
        # added = set()
        # print("peop",people)
        # while i < len(people):
        #     if people[i] >= limit:
        #         count += 1
        #         added.add(i)
        #         i +=1

        #     else:
        #         cur_w = people[i]
        #         j = i + 1
        #         while j < len(people):
        #             if ( j  not in added):
        #                 combo = cur_w + people[j]
        #                 if combo <= limit:
        #                     added.add(j)
        #                     added.add(i)
        #                     i += 1
        #                     count += 1
        #                     break
        #             j += 1
        #         if ( i not in added):
        #             count += 1
        #             added.add(i)
        #             i +=1
        # return count
            

                
    # TC O(nlogN ) + O(n2)
    # SC O(N)
      

        # APPROACH 2
        people.sort()
        l, r = 0 , len(people)-1
        count = 0
        while l <= r:
            if (people[l] + people[r] <= limit):
                
                l += 1
            # add hevaist person always
            r -= 1
            count += 1

        return count

        
        # TC O(nlog N) + O(N)
    

        