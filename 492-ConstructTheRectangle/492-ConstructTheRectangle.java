// Last updated: 2/23/2026, 6:46:52 PM
public class Solution {
    public int[] constructRectangle(int area) {
        int[] ret =  new int[2];
        
        ret[0] = area;
        ret[1] = 1;
        
        int diff = area - 1;
        
        for(int i = area - 1; i > 1; i--){
            if(area % i == 0){
                if(i < area / i) break;
                
                if(i - area / i < diff){
                    ret[0] = i;
                    ret[1] = area / i;
                }
            }
        }
        
        return ret;
    }
}