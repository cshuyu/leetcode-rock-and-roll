# Last updated: 4/5/2026, 2:17:10 PM
# Two Pointers: Merge Sort
1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        """
4        Do not return anything, modify nums1 in-place instead.
5        """
6        p1 = m-1
7        p2= n-1
8        p = m+n-1
9        while p1>=0 and p2>=0:
10            if nums1[p1]>=nums2[p2]:
11                nums1[p] = nums1[p1]
12                p1 -= 1
13            else:
14                nums1[p] = nums2[p2]
15                p2 -= 1
16            p -= 1
17        
18        while p2>=0:
19            nums1[p] = nums2[p2]
20            p2 -= 1
21            p -= 1
22
23            