class Twitter:

    def __init__(self):
        self.users_to_following = defaultdict(set)
        self.user_tweets = defaultdict(list)
        self.tweet_count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].append((self.tweet_count, tweetId))
        self.tweet_count -= 1 # python by default is a min heap so smaller number (more minus) is a newer tweet
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        self.users_to_following[userId].add(userId)
        for following in self.users_to_following[userId]:
            tweets = self.user_tweets[following]
            for i in range(len(tweets)):
                if i >= 10: break
                heapq.heappush(heap, tweets[len(tweets) - i - 1])

        res = []
        i = 0
        while heap and len(res) < 10:
            tweet_count, tweet_id = heapq.heappop(heap)
            res.append(tweet_id)

        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return
        self.users_to_following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users_to_following[followerId]:
            self.users_to_following[followerId].remove(followeeId)
