# Last updated: 2/23/2026, 6:46:22 PM
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        numOfNode = len(isConnected)
        def helper(currNode, isConnected, visited):
            nodeStack = [currNode]
            visited[currNode] = True
            while nodeStack:
                currNode = nodeStack.pop()
                for i in range(numOfNode):
                    if isConnected[currNode][i]==1 and not visited[i]:    
                        nodeStack.append(i)
                        visited[i] = True

        visited = [False]*numOfNode
        numOfComponent = 0
        for i in range(numOfNode):
            if not visited[i]:
                numOfComponent += 1
                helper(i, isConnected, visited)
        return numOfComponent
