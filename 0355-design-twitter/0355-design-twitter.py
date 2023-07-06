class Twitter:

    def __init__(self):
        self.time=0
        self.feeds={}
        self.follows={}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        self.addUser(userId)
        self.feeds[userId].append((self.time, tweetId))
    
    def addUser(self, userId):
        if self.feeds.get(userId, None) == None:
            self.feeds[userId] = []
        if self.follows.get(userId, None) == None:
            self.follows[userId] = [userId]
            
    def getNewsFeed(self, userId: int) -> List[int]:
        hp=[]
        self.addUser(userId)
        followees = set(self.follows[userId])
        for f in followees:
            idx = len(self.feeds[f])
            if idx > 0:
                time, tweet = self.feeds[f][idx-1]
                heapq.heappush(hp, (-time, tweet, f, idx-1))
        if len(hp)==0:
            return []
        ret = []
        while hp and len(ret) < 10:
            print(hp)
            time, tweet, user, idx = heapq.heappop(hp)
            ret.append(tweet)
            if idx > 0:
                time, tweet = self.feeds[user][idx-1]
                heapq.heappush(hp, (-time, tweet, user, idx-1))
        return ret
            
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.addUser(followerId)
        self.addUser(followeeId)
        self.follows[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.addUser(followerId)
        self.addUser(followeeId)
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)