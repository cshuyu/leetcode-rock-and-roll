// Last updated: 2/23/2026, 6:46:34 PM
public class Solution {
    public int findBlackPixel(char[][] picture, int N) {
        if(picture == null || picture.length == 0 || picture[0].length == 0) return 0;
        
        HashMap<Integer, ArrayList<Integer>> row = new HashMap<Integer, ArrayList<Integer>>();
        HashMap<Integer, ArrayList<Integer>> column = new HashMap<Integer, ArrayList<Integer>>();
        
        int m = picture.length;
        int n = picture[0].length;
        
        ArrayList<int[]> location = new ArrayList<int[]>();
        
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(picture[i][j] == 'B'){
                    location.add(new int[] {i,j});
                    
                    if(!row.containsKey(i)){
                        ArrayList<Integer> temp = new ArrayList<Integer>();
                        temp.add(j);
                        row.put(i, temp);
                    }
                    else{
                        row.get(i).add(j);
                    }
                    
                    if(!column.containsKey(j)){
                        ArrayList<Integer> temp1 = new ArrayList<Integer>();
                        temp1.add(i);
                        column.put(j, temp1);
                    }
                    else{
                        column.get(j).add(i);
                    }
                }
            }
        }
        
        int ret = 0;
        
        for(int[] pos : location){
            int x = pos[0];
            int y = pos[1];
            
            if(row.get(x).size() == N && column.get(y).size() == N){
                ArrayList<Integer> rows = column.get(y);
                
                boolean rule2 = true;
                for(int r : rows){
                    if(r != x){
                        if(!row.get(r).equals(row.get(x))){
                            rule2 = false;
                            break;
                        }
                    }
                }
                
                if(rule2) ret++;
            }
        }
        
        return ret;
    }
}