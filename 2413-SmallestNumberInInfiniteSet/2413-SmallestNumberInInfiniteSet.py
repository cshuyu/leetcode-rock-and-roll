# Last updated: 2/23/2026, 6:44:18 PM
class SmallestInfiniteSet:

    def __init__(self):
        self.is_present = set()
        self.added_integers = []
        self.current_integer = 1

    def popSmallest(self) -> int:
        if self.added_integers:
            res = heapq.heappop(self.added_integers)
            self.is_present.remove(res)
        else:
            res = self.current_integer
            self.current_integer += 1
        return res

    def addBack(self, num: int) -> None:
        if num >= self.current_integer or num in self.is_present:
            return
        else:
            self.is_present.add(num)
            heapq.heappush(self.added_integers, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)