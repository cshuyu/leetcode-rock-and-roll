// Last updated: 2/23/2026, 6:46:00 PM
class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        if(nums==null || nums.length==0 || k==0) {
            return 0;
        }
        int count=0;
        int product=1;
        int j=0;
        for(int i=0; i<nums.length; i++) {
            product *= nums[i];
            while(j<=i && product>=k) {
                product = product/nums[j];
                j++;
            }
            count += i-j+1;
        }
        return count;
    }
}