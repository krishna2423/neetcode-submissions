import heapq

class Twitter:

    def __init__(self):
        self.users = {} # maps follower ID to set of follower IDs that follow the key
        self.tweets = []
        self.num_tweets = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = {userId}
        self.tweets.append((-self.num_tweets, tweetId, userId))
        self.num_tweets += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        # heapify
        heap = self.tweets[:]   # copy
        heapq.heapify(heap)
        x = 10
        while x > 0 and heap:
            tweet = heapq.heappop(heap)
            if tweet[-1] in self.users[userId]:
                feed.append(tweet)
                x -= 1
        # feed = sorted(feed, key=lambda x: x[0], reverse=True)
        feed = [x[1] for x in feed]
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.users:
            self.users[followeeId] = {followeeId}
        
        if followerId not in self.users:
            self.users[followerId] = {followerId}
        
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users and followeeId in self.users[followerId]:
            if followerId != followeeId:
                self.users[followerId].remove(followeeId)
    
