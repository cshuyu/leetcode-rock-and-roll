# Last updated: 7/19/2026, 10:55:18 AM
# Backtracking
1Time: O(4^n*n)
2Space: O(n)
3class Solution:
4    def letterCombinations(self, digits: str) -> List[str]:
5        res = []
6        comb = []
7        phone_dict = {
8                        "2": ["a", "b", "c"],
9                        "3": ["d", "e", "f"],
10                        "4": ["g", "h", "i"],
11                        "5": ["j", "k", "l"],
12                        "6": ["m", "n", "o"],
13                        "7": ["p", "q", "r", "s"],
14                        "8": ["t", "u", "v"],
15                        "9": ["w", "x", "y", "z"]}
16
17        def helper(curr_idx):
18            if curr_idx == len(digits):
19                res.append("".join(comb))
20                return
21            curr_digit = digits[curr_idx]
22            letter_lst = phone_dict[curr_digit]
23            for letter in letter_lst:
24                comb.append(letter)
25                helper(curr_idx+1)
26                comb.pop()
27            
28        helper(0)
29        return res
30