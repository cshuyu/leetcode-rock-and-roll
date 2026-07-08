# Last updated: 7/8/2026, 2:30:50 PM
1class Twitter:
2
3    def __init__(self):
4        self.user_tweets = defaultdict(list)
5        self.user_followers = defaultdict(set)
6        self.timer = 0    
7
8    def postTweet(self, userId: int, tweetId: int) -> None:
9        self.timer -= 1
10        self.user_tweets[userId].append((tweetId, self.timer))
11
12    def getNewsFeed(self, userId: int) -> List[int]:
13        minHeap = []
14        res = []
15        followees = self.user_followers[userId] | {userId}
16        for followee in followees:
17            tweets_lst = self.user_tweets[followee]
18            if tweets_lst:
19                last_idx = len(tweets_lst)-1
20                tweet_id, time = tweets_lst[last_idx] 
21                heapq.heappush(minHeap, (time, tweet_id, followee, last_idx))
22
23        
24        while minHeap and len(res)<10:
25            time, tweet_id, followee, last_idx = heapq.heappop(minHeap)
26            res.append(tweet_id)
27            next_idx = last_idx-1
28
29            if next_idx>=0:
30                older_tweet_id, older_time = self.user_tweets[followee][next_idx]
31                heapq.heappush(minHeap, (older_time, older_tweet_id, followee, next_idx))
32        
33        return res
34                
35        
36    def follow(self, followerId: int, followeeId: int) -> None:
37        if followerId != followeeId:
38            self.user_followers[followerId].add(followeeId)
39
40    def unfollow(self, followerId: int, followeeId: int) -> None:
41        if followeeId in self.user_followers[followerId]:
42            self.user_followers[followerId].remove(followeeId)
43        
44
45
46# Your Twitter object will be instantiated and called as such:
47# obj = Twitter()
48# obj.postTweet(userId,tweetId)
49# param_2 = obj.getNewsFeed(userId)
50# obj.follow(followerId,followeeId)
51# obj.unfollow(followerId,followeeId)