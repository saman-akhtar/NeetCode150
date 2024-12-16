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
        self.time +=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        feed =  self.tweetMap[userId][:]
        for follwee in self.followMap[userId]:
            feed.extend(  self.tweetMap[follwee])
        feed.sort(key = lambda x:-x[0])
        return [tweetId for _,tweetId in feed[:10]]
        

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