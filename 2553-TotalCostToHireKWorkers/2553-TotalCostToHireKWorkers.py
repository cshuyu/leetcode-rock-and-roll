# Last updated: 2/23/2026, 6:44:17 PM
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        left_idx = candidates
        right_idx = n-candidates-1
        heap_left = costs[:left_idx]
        right_bound = max(candidates, right_idx+1)
        heap_right = costs[right_bound:]
        heapq.heapify(heap_left)
        heapq.heapify(heap_right)
        res = 0

        for _ in range(k):
            left_min = heap_left[0] if heap_left else float("inf")
            right_min = heap_right[0] if heap_right else float("inf")
            if left_min<=right_min:
                res += heapq.heappop(heap_left)
                if left_idx <= right_idx:
                    heapq.heappush(heap_left, costs[left_idx])
                    left_idx += 1
                
            else:
                res += heapq.heappop(heap_right)
                if left_idx <= right_idx:
                    heapq.heappush(heap_right, costs[right_idx])
                    right_idx -= 1
        
        return res
                
        