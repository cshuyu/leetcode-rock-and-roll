# Last updated: 2/26/2026, 3:06:52 PM
# Graph: Traverse(DFS)
1class Solution:
2    def exist(self, board: List[List[str]], word: str) -> bool:
3        ROWS, COLS = len(board), len(board[0])
4        visited = set() # To track the current path and avoid reusing cells
5
6        def dfs(r, c, i):
7            # 1. Base Case: We found all characters in the word!
8            if i == len(word):
9                return True
10            
11            # 2. Out of Bounds or Invalid Cell Check
12            if (
13                r < 0 or c < 0 or               # Off the top/left edge
14                r >= ROWS or c >= COLS or       # Off the bottom/right edge
15                word[i] != board[r][c] or       # Wrong letter
16                (r, c) in visited               # Already used this exact cell in the current path
17            ):
18                return False
19            
20            # 3. Choose: Mark this specific (r, c) cell as visited
21            visited.add((r, c))
22            
23            # 4. Explore: Check all 4 directions for the next letter (i + 1)
24            # If ANY direction returns True, the whole expression is True
25            found = (
26                dfs(r + 1, c, i + 1) or  # Down
27                dfs(r - 1, c, i + 1) or  # Up
28                dfs(r, c + 1, i + 1) or  # Right
29                dfs(r, c - 1, i + 1)     # Left
30            )
31            
32            # 5. Backtrack: Unmark this cell so it can be used in OTHER paths
33            visited.remove((r, c))
34            
35            return found
36
37        # 6. Start a DFS from every cell in the grid
38        for r in range(ROWS):
39            for c in range(COLS):
40                # Small optimization: only start DFS if the first letter matches
41                if board[r][c] == word[0]:
42                    if dfs(r, c, 0):
43                        return True
44                        
45        return False
46
47
48