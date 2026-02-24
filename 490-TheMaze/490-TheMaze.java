// Last updated: 2/23/2026, 6:46:53 PM
public class Solution {
    public boolean hasPath(int[][] maze, int[] start, int[] destination) {
        int x = start[0];
        int y = start[1];
        
        boolean[][] visited = new boolean[maze.length][maze[0].length];
        
        return dfs(maze, destination, x, y, visited);
    }
    
    
    private boolean dfs(int[][] maze, int[] dest, int x, int y, boolean[][] visited){
        if(x == dest[0] && y == dest[1]) return true;
        
        int[][] dirs = new int[][] {{0,1}, {0, -1}, {1, 0}, {-1, 0}};
        //reach to four different directions
        
        for(int[] d: dirs){
            int[] stop = findStopPoint(maze, x, y, d);
            int nx = stop[0];
            int ny = stop[1];
            
            if(!(nx == x && ny == y)){
               if(visited[nx][ny] == false){
                    visited[x][y] = true;
                    if(dfs(maze, dest, nx, ny, visited)) return true;
                } 
            }
            
        }
        
        return false;
    }
    
    
    private int[] findStopPoint(int[][] maze,int x, int y, int[] dir){
       int nx = x;
       int ny = y;
       
       while(nx + dir[0] >= 0 && nx + dir[0] < maze.length && ny + dir[1] >= 0 && ny + dir[1] < maze[0].length && maze[nx + dir[0]][ny + dir[1]] != 1){
           nx = nx + dir[0];
           ny = ny + dir[1];
       }
       
       return new int[] {nx, ny};
    }
}