// Last updated: 2/23/2026, 6:46:03 PM
class Solution {
    public int numDistinctIslands(int[][] grid) {
        boolean[][] seen = new boolean[grid.length][grid[0].length];
        Set<String> shapes = new HashSet<>();
        StringBuilder sb = new StringBuilder();
        
        for(int r=0; r<grid.length; r++) {
            for(int c=0; c<grid[0].length; c++) {
                sb = new StringBuilder();
                explore(r, c, r, c, seen, grid, sb);
                // System.out.println(sb.toString());
                if(sb!=null && sb.length()!=0)
                    shapes.add(sb.toString());
            }
        }
        // for(String shape : shapes) {
        //     System.out.println("Shape: "+shape);
        // }
        return shapes.size();
    }
    
    public void explore(int r, int c, int r0, int c0, boolean[][] seen, int[][] grid, StringBuilder sb) {
        if(0<=r && r<grid.length && 0<=c && c<grid[0].length && grid[r][c]==1 && !seen[r][c]) {
            seen[r][c] = true;
            sb.append("("+String.valueOf(r-r0)+","+String.valueOf(c-c0)+")");
            explore(r-1, c, r0, c0, seen, grid, sb);
            explore(r+1, c, r0, c0, seen, grid, sb);
            explore(r, c-1, r0, c0, seen, grid, sb);
            explore(r, c+1, r0, c0, seen, grid, sb);
        }
    }
}