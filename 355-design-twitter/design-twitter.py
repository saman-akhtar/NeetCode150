class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list) # userKey : [posts]
        # self.userIds = {
        #     user:{
        #         post:{},
        #         folower:{},
        #         followee: {}
        # }
        self.followMap= defaultdict(set) # id: [id1,id2]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        # self.time +=1 #approach 1
        self.time -=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # approach 2
        self.followMap[userId].add(userId)
        minHeap = []
        res = []
        for followeeId in self.followMap[userId]:
            # edge case ass check
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId])-1
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count, tweetId,  followeeId, index -1] )
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index =  heapq.heappop(minHeap)
            res.append(tweetId)
            if index >=0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index -1 ])
        return res





        #Approach 1
    #     feed =  self.tweetMap[userId][:]
    #     for follwee in self.followMap[userId]:
    #         feed.extend(  self.tweetMap[follwee])
    #     feed.sort(key = lambda x:-x[0])
    #     return [tweetId for _,tweetId in feed[:10]]
    
    # # O(NlogN where N=U+T , u = total no of tweet by cur user, Tc = total no of twee of follower)
#  , the total number of tweets in the feed.
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if( followerId != followeeId):
            self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)