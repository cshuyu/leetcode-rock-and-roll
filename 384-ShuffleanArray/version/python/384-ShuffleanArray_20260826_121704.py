# Last updated: 8/26/2026, 12:17:04 PM
1"""
2O(Time): reset: O(n), shuffle: O(n)
3O(Space): O(n)
4"""
5class Solution:
6
7    def __init__(self, nums: List[int]):
8        self.original = list(nums)
9        self.array = list(nums)
10
11    def reset(self) -> List[int]:
12        self.array = list(self.original)
13        return self.array
14
15    def shuffle(self) -> List[int]:
16        arr_length = len(self.array)
17        for i in range(arr_length):
18            j = i + random.randint(0, arr_length-1-i)
19            self.array[i], self.array[j] = self.array[j], self.array[i]
20        return self.array
21
22
23# Your Solution object will be instantiated and called as such:
24# obj = Solution(nums)
25# param_1 = obj.reset()
26# param_2 = obj.shuffle()
27
28