// Last updated: 2/23/2026, 6:45:58 PM
class Solution {
    public int pivotIndex(int[] nums) {
        if (nums.length < 0) return -1;
        if (nums.length == 1) return 0;
        int[] sums = new int[nums.length];
        sums[0] = nums[0];
        for(int i=1; i<nums.length; i++) {
            sums[i] = sums[i-1] + nums[i];
        }

        for(int i=0; i<sums.length; i++) {
            int leftSum = (i == 0? 0 : sums[i-1]);
            int rightSum = sums[sums.length - 1] - sums[i];
            if (leftSum == rightSum) {
                return i;
            }
        }
        return -1;
    }
}