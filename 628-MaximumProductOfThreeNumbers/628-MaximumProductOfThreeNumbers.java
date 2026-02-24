// Last updated: 2/23/2026, 6:46:16 PM
class Solution {
    public int maximumProduct(int[] nums) {
        if(nums==null || nums.length < 3)
            return 0;
        
        int[] tmp = {nums[0], nums[1], nums[2]};
        Arrays.sort(tmp);
        
        int max1 = tmp[2];
        int max2 = tmp[1];
        int max3 = tmp[0];
        int min1 = tmp[0];
        int min2 = tmp[1];
        
        for(int i=3; i<nums.length; i++) {
            if(nums[i]>max1) {
                max3 = max2;
                max2 = max1;
                max1 = nums[i];
            } else if(max2<nums[i]) {
                max3 = max2;
                max2 = nums[i];
            } else if(max3<nums[i])
                max3 = nums[i];
            
            if(nums[i] < min1) {
                min2 = min1;
                min1 = nums[i];
            } else  if(nums[i] <min2)
                min2 = nums[i];
        }
        return Math.max(max1*max2*max3, min1*min2*max1);
    }
}