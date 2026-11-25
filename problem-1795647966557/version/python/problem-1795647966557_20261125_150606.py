# Last updated: 11/25/2026, 3:06:06 PM
# Iterator: stack
1# """
2# This is the interface that allows for creating nested lists.
3# You should not implement it, or speculate about its implementation
4# """
5#class NestedInteger:
6#    def isInteger(self) -> bool:
7#        """
8#        @return True if this NestedInteger holds a single integer, rather than a nested list.
9#        """
10#
11#    def getInteger(self) -> int:
12#        """
13#        @return the single integer that this NestedInteger holds, if it holds a single integer
14#        Return None if this NestedInteger holds a nested list
15#        """
16#
17#    def getList(self) -> [NestedInteger]:
18#        """
19#        @return the nested list that this NestedInteger holds, if it holds a nested list
20#        Return None if this NestedInteger holds a single integer
21#        """
22
23class NestedIterator:
24    def __init__(self, nestedList: [NestedInteger]):
25        self.stack = nestedList[::-1]
26    
27    def next(self) -> int:
28        if not self.hasNext():
29            raise NoIterationError(Exception)
30        return self.stack.pop().getInteger()
31        
32    def hasNext(self) -> bool:
33        while self.stack:
34            top = self.stack[-1]
35            if top.isInteger():
36                return True
37            self.stack.pop()
38            self.stack.extend(top.getList()[::-1])
39        return False
40
41            
42
43# Your NestedIterator object will be instantiated and called as such:
44# i, v = NestedIterator(nestedList), []
45# while i.hasNext(): v.append(i.next())
46
47