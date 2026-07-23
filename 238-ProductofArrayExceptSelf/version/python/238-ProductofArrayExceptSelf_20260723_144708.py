# Last updated: 7/23/2026, 2:47:08 PM
# prefix_sum
1"""
2Time: O(n)
3Space: O(1)
4"""
5class Solution:
6    def productExceptSelf(self, nums: List[int]) -> List[int]:
7        res = [1]*(len(nums))
8        # from left to right
9        for i in range(1, len(nums)):
10            res[i] = res[i-1]*nums[i-1]
11        
12        # from right to left
13        product_right = 1
14        for j in range(len(nums)-2, -1, -1):
15            product_right = product_right*nums[j+1]
16            res[j] = res[j]*product_right
17        return res
18