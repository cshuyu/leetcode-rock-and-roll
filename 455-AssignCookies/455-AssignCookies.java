// Last updated: 2/23/2026, 6:47:10 PM
public class Solution {
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);
    
        int ret = 0;
        int kidIndex = 0;
        int cookieIndex = 0;
        
        while(kidIndex < g.length && cookieIndex < s.length){
            int demand = g[kidIndex];
            int supply = s[cookieIndex];
            
            if(supply >= demand){
                ret++;
                kidIndex++;
                cookieIndex++;
            }
            else{
                cookieIndex++;
            }
        }
        
        return ret;
    }
}