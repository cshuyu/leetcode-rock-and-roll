// Last updated: 2/23/2026, 6:47:05 PM
public class Solution {
    public int minMoves2(int[] nums) {
        int ret = 0;
        int l = 0;
        int r = nums.length -1 ;
        
        Arrays.sort(nums);
        
        while(l < r){
            ret += nums[r] - nums[l];
            l++;
            r--;
        }
        
        return ret;
    }
}