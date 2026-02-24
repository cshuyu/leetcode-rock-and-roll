// Last updated: 2/23/2026, 6:46:19 PM
class Solution {
    public int arrayPairSum(int[] nums) {
        Arrays.sort(nums);
        int res = 0;
        int i = 0;
        while(i<nums.length) {
            res += nums[i];
            i += 2;
        }
        return res;
    }
}