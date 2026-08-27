# Last updated: 8/27/2026, 4:21:26 PM
# Random
1"""
2When there is lots of call of pick，we choose this way
3O(Time): initialize: O(n), pick: O(1)
4O(Space): initialize: O(n), pick: O(1)
5"""
6class Solution:
7    def __init__(self, nums: List[int]):
8        self.mapping = defaultdict(list)
9        for i in range(len(nums)):
10            self.mapping[nums[i]].append(i)
11
12
13    def pick(self, target: int) -> int:
14        lst = self.mapping[target]
15        lst_length = len(lst)
16        idx = random.randint(0, lst_length-1)
17        return lst[idx]
18        
19
20
21# Your Solution object will be instantiated and called as such:
22# obj = Solution(nums)
23# param_1 = obj.pick(target)