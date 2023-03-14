"""
Leetcode Problem
https://leetcode.com/problems/design-twitter/
"""
class Twitter(object):

    def __init__(self):
        # Use defaultdict and deque to store tweets for each user
        self.tweets = collections.defaultdict(deque)
        self.follows = defaultdict(set) #key userId1 value [userId2] userId1 follows userId2
        self.timestamp = 0

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.timestamp += 1
        self.tweets[userId].appendleft((-self.timestamp, tweetId))
        # If the deque for the user has more than 10 tweets, remove the oldest tweet from the right
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop()


    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        # Merge the tweets of the user's followees (including the user) using heapq.merge
        tweets = list(heapq.merge(
            *(self.tweets[followee] for followee in self.follows[userId] | {userId})))
        # Return the tweet IDs of the 10 most recent tweets
        return [tweetId for _, tweetId in tweets[:10]]


    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.follows[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
