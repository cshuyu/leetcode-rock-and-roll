# Last updated: 7/12/2026, 3:48:45 PM
# Two Pointer + heap
1"""
2It is similar with the problem of merge k sorted list
3Each time, we add nums1[index] with each of nums2's current smalllest unchecked element
4Time: O(klogmin(m,k))
5Space: O(min(m,k))
6"""
7class Solution:
8    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
9        res = []
10        if not nums1 or not nums2 or k==0:
11            return res
12        min_heap = []
13        for i in range(min(len(nums1), k)):
14            heapq.heappush(min_heap, (nums1[i]+nums2[0], i, 0))
15        
16        while len(res)<k:
17            curr_min, i, j = heapq.heappop(min_heap)
18            res.append([nums1[i], nums2[j]])
19
20            if j+1<len(nums2):
21                heapq.heappush(min_heap, (nums1[i]+nums2[j+1], i, j+1))
22        
23        return res
24