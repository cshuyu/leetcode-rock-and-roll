// Last updated: 2/23/2026, 6:47:16 PM
public class Solution {
    public int numberOfBoomerangs(int[][] points) {
        if(points == null || points.length == 0) return 0;
        int count = 0;
        
         
        for(int i = 0; i < points.length; i++){
            HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
            //HashSet<Integer> set = new HashSet<Integer>();
            for(int j = 0; j < points.length; j++){
                if(i != j){
                    int x = points[i][0] - points[j][0];
                    int y = points[i][1] - points[j][1];
                    int dis = x * x + y * y;
                    map.put(dis, map.getOrDefault(dis, 0) + 1);
                }
            }
            
            for(Integer size: map.values()){
                count += size * (size - 1);
            }
        }
        
        return count;
    }
    
}