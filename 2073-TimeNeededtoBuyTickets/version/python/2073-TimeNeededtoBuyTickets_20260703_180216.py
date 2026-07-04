# Last updated: 7/3/2026, 6:02:16 PM
# Queue
1"""
2Time: O(m*n)
3Space: O(n)
4"""
5class Solution:
6    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
7        ticket_queue = deque()
8        for index in range(len(tickets)):
9            ticket_queue.append((index, tickets[index]))
10        time = 0
11        
12        while ticket_queue:
13            index, ticket_left = ticket_queue.popleft()
14            ticket_left -= 1
15            time += 1
16            if index==k and ticket_left==0:
17                return time
18            elif ticket_left>0:
19                ticket_queue.append((index, ticket_left))
20        
21        return -1
22
23