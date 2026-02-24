// Last updated: 2/23/2026, 6:46:24 PM
public class Solution {
    public String findContestMatch(int n) {
        HashMap<Integer, String> map = new HashMap<Integer,String>();
        boolean firstRound = true;
        
        while(n > 1){
            int mid = n / 2;
            
            for(int i = 1; i <= mid; i++){
                if(firstRound){
                    map.put(i, "(" + i + "," + (n + 1 - i) + ")");
                }
                else{
                    map.put(i, "(" + map.get(i) + "," + map.get(n + 1 - i) +")");
                }
            }
            firstRound = false;
            
            n = n / 2;
        }
        
        return map.get(1);
    }
}