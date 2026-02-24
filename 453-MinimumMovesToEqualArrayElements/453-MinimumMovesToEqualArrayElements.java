// Last updated: 2/23/2026, 6:47:12 PM
public class Solution {
    public int minMoves(int[] nums) {
        int sum = 0;
        int min = Integer.MAX_VALUE;
        
        for(int num: nums){
            sum += num;
            min = Math.min(min, num);
        }
        
        return sum - min * nums.length;
    }
}