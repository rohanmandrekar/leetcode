class Twitter:

    def __init__(self):
        self.following=defaultdict(set)
        self.count=0
        self.tweet=defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append([self.count,tweetId])
        self.count-=1
    
    def getNewsFeed(self, userId: int) -> List[int]:
        ans=[]
        minheap=[]
        self.following[userId].add(userId)
        for followeeId in self.following[userId]:
            if followeeId in self.tweet:
                index=len(self.tweet[followeeId])-1
                count,tweetid = self.tweet[followeeId][index]
                minheap.append([count,tweetid,followeeId,index-1])
        heapq.heapify(minheap)

        while minheap and len(ans)<10:
            count,tweet,followeeId,index=heapq.heappop(minheap)
            ans.append(tweet)
            if index>=0:
                count,tweetId=self.tweet[followeeId][index]
                heapq.heappush(minheap,[count,tweetId,followeeId,index-1])
        return ans        


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)