# Last updated: 3/15/2026, 1:21:48 AM
1class Solution:
2    def minJumps(self, arr: List[int]) -> int:
3        # Time complexity: set_map O(n)+go_through_queue O(n), total is O(n)
4        # Space complexity: set_map O(n)+visited O(n)+queue<O(n), total is O(n)
5        valueMap = defaultdict(list)
6        for i in range(len(arr)):
7            valueMap[arr[i]].append(i)
8        # add [val, index, step] to queue
9        queue = deque([(arr[0], 0, 0)])
10        # a set of idx
11        visited = set()
12        visited.add(0)
13        while queue:
14            curr_val, curr_idx, step = queue.popleft()
15            if curr_idx == len(arr)-1:
16                return step
17            if curr_idx-1>=0 and curr_idx-1 not in visited:
18                queue.append((arr[curr_idx-1], curr_idx-1, step+1))
19                visited.add(curr_idx-1)
20            if curr_idx+1<len(arr) and curr_idx+1 not in visited:
21                queue.append((arr[curr_idx+1], curr_idx+1, step+1))
22                visited.add(curr_idx+1)
23            for idx in valueMap.pop(curr_val, []):
24                if idx not in visited:
25                    queue.append((arr[idx], idx, step+1))
26                    visited.add(idx)
27        return -1
28
29            
30
31
32
33