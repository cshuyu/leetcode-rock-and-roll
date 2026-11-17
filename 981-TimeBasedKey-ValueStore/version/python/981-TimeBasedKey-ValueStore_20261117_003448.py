# Last updated: 11/17/2026, 12:34:48 AM
# hashMap+binary_search
1'''
2O(Time): set->O(1), get->O(logn) 
3O(Space): O(n)
4'''
5class TimeMap:
6
7    def __init__(self):
8        self.map = defaultdict(list)
9
10    def set(self, key: str, value: str, timestamp: int) -> None:
11        self.map[key].append((value, timestamp))
12
13    def get(self, key: str, timestamp: int) -> str:
14        if key not in self.map:
15            return ""
16        timebased_list = self.map[key]
17        left_idx = 0
18        right_idx = len(timebased_list)-1
19        while left_idx<right_idx-1:
20            mid_idx = left_idx + (right_idx-left_idx)//2
21            curr_timestamp = timebased_list[mid_idx][1]
22            if timestamp == curr_timestamp:
23                return timebased_list[mid_idx][0]
24            elif timestamp < curr_timestamp:
25                right_idx = mid_idx - 1
26            else:
27                left_idx = mid_idx
28        if timebased_list[right_idx][1]<=timestamp:
29            return timebased_list[right_idx][0]
30        elif timebased_list[left_idx][1] <= timestamp:
31            return timebased_list[left_idx][0]
32        else:
33            return ""
34        
35
36
37# Your TimeMap object will be instantiated and called as such:
38# obj = TimeMap()
39# obj.set(key,value,timestamp)
40# param_2 = obj.get(key,timestamp)