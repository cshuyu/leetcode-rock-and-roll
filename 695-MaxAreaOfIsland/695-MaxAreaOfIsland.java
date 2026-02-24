// Last updated: 2/23/2026, 6:46:02 PM
class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int ans = 0;
        for(int r=0; r<grid.length; r++) {
            for(int c=0; c<grid[0].length; c++) {
                if(grid[r][c] == 1)
                    ans = Math.max(ans, AreaOfIsland(grid, r, c));
            }
        }
        return ans;
    }
    
    public int AreaOfIsland(int[][]grid, int r, int c) {
        if(r>=0 && r<grid.length && c>=0 && c<grid[0].length && grid[r][c]==1) {
            grid[r][c] = 0;
            return 1+AreaOfIsland(grid,r+1,c)+AreaOfIsland(grid,r-1,c)+AreaOfIsland(grid,r,c-1)+AreaOfIsland(grid,r,c+1);
        }
        return 0;
    }
}