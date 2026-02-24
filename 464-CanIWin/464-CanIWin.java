// Last updated: 2/23/2026, 6:47:04 PM
class Solution {
    Map<Integer, Boolean> UsedIntegerMap;
    public boolean canIWin(int maxChoosableInteger, int desiredTotal) {
        boolean[] visited = new boolean[maxChoosableInteger+1];
        UsedIntegerMap = new HashMap<Integer, Boolean>();
        int maxSum = maxChoosableInteger*(1+maxChoosableInteger)/2;
        if(desiredTotal>maxSum)
            return false;
        else if(desiredTotal<=0)
            return true;
        return helper(desiredTotal, visited);
    }
    
    private boolean helper(int desiredTotal, boolean[] visited) {
        if(desiredTotal<=0)
            return false;
        int key = format(visited);
        if(!UsedIntegerMap.containsKey(key)) {
            for(int i=1; i<visited.length; i++) {
                if(visited[i])
                    continue;
                else {
                    visited[i] = true;
                    int currentTotalVal = desiredTotal-i;
                    if(!helper(currentTotalVal, visited)) {
                        UsedIntegerMap.put(key, true);
                        visited[i] = false;
                        return true;
                    }
                    visited[i] = false;
                }
            }
            UsedIntegerMap.put(key, false);
            return false;
        }
        return UsedIntegerMap.get(key);
    }
    
    public int format(boolean[] used){
        int num = 0;
        for(boolean b: used){
            num <<= 1;
            if(b) num |= 1;
        }
        return num;
    }
}






// visited array boolean[]
// helper(currentTotalVal)->return boolean
// Map<format(visited array), Boolean>--> desiredTotal
