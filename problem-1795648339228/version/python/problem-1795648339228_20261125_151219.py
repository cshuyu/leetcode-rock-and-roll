# Last updated: 11/25/2026, 3:12:19 PM
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
22"""
23O(next)/O(hasNext) avg->O(1), 
24O(space) O(max_D)-> max_D is the max depth of nexted lists
25"""
26class NestedIterator:
27    def __init__(self, nestedList: [NestedInteger]):
28        self.stack = nestedList[::-1]
29    
30    def next(self) -> int:
31        if not self.hasNext():
32            raise NoIterationError(Exception)
33        return self.stack.pop().getInteger()
34        
35    def hasNext(self) -> bool:
36        while self.stack:
37            top = self.stack[-1]
38            if top.isInteger():
39                return True
40            self.stack.pop()
41            self.stack.extend(top.getList()[::-1])
42        return False
43
44            
45
46# Your NestedIterator object will be instantiated and called as such:
47# i, v = NestedIterator(nestedList), []
48# while i.hasNext(): v.append(i.next())
49
50