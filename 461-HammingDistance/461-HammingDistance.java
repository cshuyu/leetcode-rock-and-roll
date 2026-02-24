// Last updated: 2/23/2026, 6:47:06 PM
public class Solution {
    public int hammingDistance(int x, int y) {
        int count = 0;
        int xor = x ^ y;
        
        for(int i = 0; i < 32; i++){
            if((xor & 1) == 1) count++;
            xor = xor >>> 1;
        }
        
        return count;
    }
}