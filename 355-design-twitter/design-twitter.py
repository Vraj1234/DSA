class Twitter:

    def __init__(self):
        self.time = 0
        self.posts = defaultdict(list)
        self.following = defaultdict(set)
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.time, tweetId))
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.following[userId] | {userId}
        heap = []
        res = []
        for user in users:
            if self.posts[user]:
                idx = len(self.posts[user])-1
                ts, id = self.posts[user][-1][0], self.posts[user][-1][1]
                ts = -ts
                heapq.heappush(heap, (ts, id, user, idx))
        
        while heap and len(res) < 10:
            ts, id, user, idx = heapq.heappop(heap)
            res.append(id)
            if idx>0:
                idx -=1
                ts, id = self.posts[user][idx]
                ts = -ts
                heapq.heappush(heap, (ts, id, user, idx))

    
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)