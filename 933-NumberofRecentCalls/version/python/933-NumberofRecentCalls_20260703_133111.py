# Last updated: 7/3/2026, 1:31:11 PM
# Queue
1"""
2Time: amortized O(1)
3Space: O(n)
4"""
5class RecentCounter:
6
7    def __init__(self):
8        self.counter_queue = deque()
9
10    def ping(self, t: int) -> int:
11        self.counter_queue.append(t)
12        while self.counter_queue and self.counter_queue[0]<t-3000:
13            self.counter_queue.popleft()
14        return len(self.counter_queue)
15
16
17# Your RecentCounter object will be instantiated and called as such:
18# obj = RecentCounter()
19# param_1 = obj.ping(t)
20
21