# Last updated: 11/20/2026, 11:53:31 PM
# Get Random + hashmap + list
1'''
2O(insert): O(1)
3O(remove): O(1)
4O(getRandom): O(1)
5O(space): O(n)
6'''
7import random
8class RandomizedSet:
9
10    def __init__(self):
11        self.val_to_idx = defaultdict(int)
12        self.nums = []
13
14    def insert(self, val: int) -> bool:
15        if val in self.val_to_idx:
16            return False
17        self.val_to_idx[val] = len(self.nums)
18        self.nums.append(val)
19        return True
20
21    def remove(self, val: int) -> bool:
22        if val not in self.val_to_idx:
23            return False
24        idx = self.val_to_idx[val]
25        tmp = self.nums[-1]
26        self.nums[idx] = tmp
27        self.val_to_idx[tmp] = idx
28        self.nums.pop()
29        del self.val_to_idx[val]
30        return True
31
32    def getRandom(self) -> int:
33        rand_idx = random.randint(0, len(self.nums)-1)
34        return self.nums[rand_idx]
35        
36
37
38# Your RandomizedSet object will be instantiated and called as such:
39# obj = RandomizedSet()
40# param_1 = obj.insert(val)
41# param_2 = obj.remove(val)
42# param_3 = obj.getRandom()