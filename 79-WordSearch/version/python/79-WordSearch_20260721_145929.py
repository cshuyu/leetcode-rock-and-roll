# Last updated: 7/21/2026, 2:59:29 PM
# Backtracking
1"""
2O(Time): M*N*3^L
3O(Space):L+M*N
4"""
5class Solution:
6    def exist(self, board: List[List[str]], word: str) -> bool:
7        char_to_coords = defaultdict(list)
8        for row in range(len(board)):
9            for col in range(len(board[0])):
10                letter = board[row][col]
11                char_to_coords[letter].append((row, col))
12        
13        first_char = word[0]
14        if not char_to_coords[first_char]:
15            return False
16        
17        def helper(r, c, index):
18            if index == len(word):
19                return True
20            if r<0 or c<0 or r>=len(board) or c>=len(board[0]) or board[r][c]!=word[index]:       
21                return False
22            temp = board[r][c]
23            board[r][c] = "0"
24            found = helper(r+1, c, index+1) or helper(r-1, c, index+1) or helper(r, c-1, index+1) or helper(r, c+1, index+1)
25            board[r][c] = temp
26            return found
27        
28        for coords in char_to_coords[first_char]:
29            row, col = coords
30            if helper(row, col, 0):
31                return True
32        return False
33