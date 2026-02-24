// Last updated: 2/23/2026, 6:46:38 PM
class Solution {
    public int change(int amount, int[] coins) {
        if(amount == 0) {
            return 1;
        } else if (coins.length == 0) {
            return 0;
        }
        
        // Arrays.sort(coins);
        int[] b = new int[amount+1];
        b[0] = 1;
       
        // For one dimension space, we should always update
        // vertically to make sure that b[w] stores the value
        // for coins [1...i] before updating b[w].
        for(int i=0; i<coins.length; i++) { 
            for(int w=1; w<=amount; w++) {
                int v = coins[i];
                if(v > w) {
                    // so that b[w] still stores the value
                    // with coins [1...i-1]
                    continue;
                } 
                // b[w-v] stores the value for coin [1...i].
                b[w] += b[w - v]; 
            }
        }
        
        return b[amount];
    }
}