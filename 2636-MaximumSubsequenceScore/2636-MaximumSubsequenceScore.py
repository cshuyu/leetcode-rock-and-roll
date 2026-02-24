# Last updated: 2/23/2026, 6:44:14 PM
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = sorted(zip(nums1, nums2), key=lambda x: x[1], reverse=True)

        min_heap = []
        current_sum = 0
        max_total_score = 0

        for n1, n2 in pairs:
            heapq.heappush(min_heap, n1)
            current_sum += n1

            if len(min_heap) > k:
                current_sum -= heapq.heappop(min_heap)
            
            if len(min_heap) == k:
                max_total_score = max(max_total_score, current_sum*n2)
        
        return max_total_score