# Last updated: 2/23/2026, 6:45:10 PM
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []

        def helper(node, curr_lst):
            curr_lst.append(node)
            if node == len(graph)-1:
                res.append(list(curr_lst))
            else:
                for next_node in graph[node]:
                    helper(next_node, curr_lst)
            curr_lst.pop()
        
        helper(0, [])
        return res




        