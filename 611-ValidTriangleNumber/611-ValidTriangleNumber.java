// Last updated: 2/23/2026, 6:46:18 PM
class Solution {
    public int triangleNumber(int[] nums) {
        int count = 0;
        Arrays.sort(nums);
        for(int i=0; i<nums.length-2; i++) {
            int k=i+2;
            for(int j=i+1; j<nums.length-1; j++) {
                while(k<nums.length && nums[i]+nums[j]>nums[k]) {
                    k++;
                    // System.out.println("k: "+k+", j: "+j);
                }    
                count += Math.max(0, k-j-1);
                // System.out.println("count: "+count);
            }
        }
        return count;
    }
}