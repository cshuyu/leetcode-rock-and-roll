// Last updated: 2/23/2026, 6:46:27 PM
public class Solution {
    public List<List<Integer>> updateMatrix(List<List<Integer>> matrix) {
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        
        int m = matrix.size();
        int n = matrix.get(0).size();
        
        int[][] distance = new int[m][n];
        boolean[][] visited = new boolean[m][n];
        
        Queue<int[]> queue = new LinkedList<int[]>();
        
        int level = 0;
        
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(matrix.get(i).get(j) == 0){
                    queue.add(new int[]{i ,j});
                    visited[i][j] = true;
                }
            }
        }
        
        int[][] dirs = {{1,0}, {-1, 0}, {0, 1}, {0, -1}};
        int count = 0;
        int size = queue.size();
        
        while(queue.isEmpty() == false){
            int[] top = queue.poll();
            int x = top[0];
            int y = top[1];
            distance[x][y] = level;
            count++;
            
            for(int[] dir : dirs){
                int nx = x + dir[0];
                int ny = y + dir[1];
                
                if(nx >= 0 && nx < m && ny >= 0 && ny < n && visited[nx][ny] == false){
                    visited[nx][ny] = true;
                    queue.offer(new int[] {nx, ny});
                }
            }
            
            if(count == size){
                count = 0;
                size = queue.size();
                level++;
            }
        }
        
        for(int i = 0; i < m; i++){
            List<Integer> tmp = new ArrayList<Integer>();
            
            for(int j = 0; j < n; j++){
                tmp.add(distance[i][j]);
            }
            
            ret.add(tmp);
        }
        
        return ret;
        
    }
}