# Last updated: 7/8/2026, 2:52:47 PM
1class Twitter:
2    def __init__(self):
3        self.tweet_dict = defaultdict(list)
4        self.follower_dict = defaultdict(set)
5        self.timer = 0
6    # O(1)
7    def postTweet(self, userId: int, tweetId: int) -> None:
8        self.timer -= 1
9        self.tweet_dict[userId].append((tweetId, self.timer))
10    # O(f+10logf), f is amount of followers
11    def getNewsFeed(self, userId: int) -> List[int]:
12        min_heap = []
13        res = []
14        feed_users = self.follower_dict[userId] | {userId}
15        for feed_user in feed_users:
16            tweet_lst = self.tweet_dict[feed_user]
17            if tweet_lst:
18                idx = len(tweet_lst)-1
19                tweet_id, time = tweet_lst[idx]
20                min_heap.append((time, tweet_id, feed_user, idx))
21        heapq.heapify(min_heap)
22        
23        while min_heap and len(res)<10:
24            _, tweet_id, feed_user, idx = heapq.heappop(min_heap)
25            res.append(tweet_id)
26            next_idx = idx - 1
27            if next_idx >= 0:
28                next_tweet_id, next_time = self.tweet_dict[feed_user][next_idx]
29                heapq.heappush(min_heap, (next_time, next_tweet_id, feed_user, next_idx))
30        return res
31    # O(1)
32    def follow(self, followerId: int, followeeId: int) -> None:
33        self.follower_dict[followerId].add(followeeId)
34    # O(1)
35    def unfollow(self, followerId: int, followeeId: int) -> None:
36        if followeeId in self.follower_dict[followerId]:
37            self.follower_dict[followerId].remove(followeeId)
38        
39
40# Your Twitter object will be instantiated and called as such:
41# obj = Twitter()
42# obj.postTweet(userId,tweetId)
43# param_2 = obj.getNewsFeed(userId)
44# obj.follow(followerId,followeeId)
45# obj.unfollow(followerId,followeeId)