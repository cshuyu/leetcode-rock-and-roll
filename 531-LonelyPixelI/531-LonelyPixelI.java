// Last updated: 2/23/2026, 6:46:35 PM
public class Solution {
    public int findLonelyPixel(char[][] picture) {
        if(picture == null || picture.length == 0 || picture[0].length == 0) return 0;
        
        int m = picture.length;
        int n = picture[0].length;
        
        boolean[] row = new boolean[m];
        boolean[] column = new boolean[n];
        
        ArrayList<int[]> location = new ArrayList<int[]>();
        
        for(int i = 0; i < m; i++){
            int count = 0;
            for(int j = 0; j < n; j++){
                if(picture[i][j] == 'B'){
                    location.add(new int[] {i,j});
                    count++;
                }
            }
            if(count > 1) row[i] = true;
        }
        
        for(int i = 0; i < n; i++){
            int count = 0;
            for(int j = 0; j < m; j++){
                if(picture[j][i] == 'B'){
                    count++;
                }
            }
            if(count > 1) column[i] = true;
        }
        
        int ret = 0;
        
        for(int[] position : location){
            int x = position[0];
            int y = position[1];
            
            if(!row[x] &&!column[y]){
                ret++;
            }
        }
        
        return ret;
    }
}