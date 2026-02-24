// Last updated: 2/23/2026, 6:46:07 PM
class Solution {
    public int findLengthOfLCIS(int[] nums) {
        if(nums==null || nums.length==0)
            return 0;
        int[] temp = new int[nums.length];
        temp[0] = 1;
        int currMax = temp[0];
        for(int i=0; i<nums.length-1; i++) {
            if(nums[i]<nums[i+1])
                temp[i+1] = temp[i] + 1;
            else
                temp[i+1] = 1;
            currMax = Math.max(currMax, temp[i+1]);
        }
        return currMax;
    }
}