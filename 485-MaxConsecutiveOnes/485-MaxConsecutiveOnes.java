// Last updated: 2/23/2026, 6:46:55 PM
public class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        if(nums == null || nums.length == 0) return 0;
        
        int max = 0;
        
        int count = 0;
        
        for(int i : nums){
            if(i == 1){
                count++;
                max = Math.max(max, count);
            }
            else{
                count = 0;
            }
        }
        
        return max;
    }
}