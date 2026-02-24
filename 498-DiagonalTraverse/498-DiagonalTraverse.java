// Last updated: 2/23/2026, 6:46:49 PM
public class Solution {
    public int[] findDiagonalOrder(int[][] matrix) {
        if(matrix == null || matrix.length == 0 || matrix[0].length == 0) return new int[0];
        
        int m = matrix.length;
        int n = matrix[0].length;
        
        boolean up = true;
        int x = 0;
        int y = 0;
        int count = 1;
        
        ArrayList<Integer> list = new ArrayList<Integer>();
        
        list.add(matrix[x][y]);
        
        while(count < m * n){
            if(up){
                int nextX = x - 1;
                int nextY = y + 1;
                //valid up forward
                if(nextX >= 0 && nextY < n){
	                    x = nextX;
	                    y = nextY;
	                }
	                else if(nextX >= 0 && nextY >= n){
	                    x = x + 1;
	                    up = false;
	                }
	                else if (nextX < 0 && nextY < n){
	                    y = y + 1;
	                    up = false;
	                }
	                else if (nextX < 0 && nextY >= n){
	                	x = x + 1;
	                	up = false;
	                }
                //eventually
                list.add(matrix[x][y]);
                count++;
            }
            else{
                int nextX = x + 1;
                int nextY = y - 1;
                
                if(nextX < m && nextY >=0){
                    x = nextX;
                    y = nextY;
                }
                // else if(nextX >= m && nextY >= 0){
                //     y = y + 1;
                //     up = true;
                // }
                // else if(nextX >= m && nextY < 0){
                //     y = y + 1;
                //     up = true;
                // }
                else if(nextX < m && nextY < 0){
                    x = x + 1;
                    up = true;
                }
                else if(nextX >= m){
                    y = y + 1;
                    up = true;
                }
                list.add(matrix[x][y]);
                count++;
            }
        }
        
        int[] ret = new int[list.size()];
        for(int i = 0; i < list.size(); i++){
            ret[i] = list.get(i);
        }
        return ret;
    }
}