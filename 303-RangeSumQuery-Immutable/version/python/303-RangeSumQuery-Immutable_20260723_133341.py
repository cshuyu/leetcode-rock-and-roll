# Last updated: 7/23/2026, 1:33:41 PM
# prefix_sum
1"""
2Initialize:
3O(Time): O(n), O(Space):O(n)
4sumRange:
5O(Time),O(space): O(1)
6prefix_sum[i] is not include i
7"""
8class NumArray:
9    def __init__(self, nums: List[int]):
10        self.prefix_sum = [0]*(len(nums)+1)
11        for i in range(1, len(nums)+1):
12            self.prefix_sum[i] += self.prefix_sum[i-1] + nums[i-1]
13
14    def sumRange(self, left: int, right: int) -> int:
15        return self.prefix_sum[right+1]-self.prefix_sum[left]
16
17
18# Your NumArray object will be instantiated and called as such:
19# obj = NumArray(nums)
20# param_1 = obj.sumRange(left,right)
21
22