# Last updated: 7/3/2026, 5:18:59 PM
1class Solution:
2    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
3        time = 0
4        for i in range(k+1):
5            if tickets[i]<tickets[k]:
6                time += tickets[i]
7            else:
8                time += tickets[k]
9        
10        for j in range(k+1, len(tickets)):
11            if tickets[j]<tickets[k]-1:
12                time += tickets[j]
13            else:
14                time += tickets[k]-1
15        return time
16
17
18            
19
20
21
22