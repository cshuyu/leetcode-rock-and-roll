// Last updated: 2/23/2026, 6:46:51 PM
public class Solution {
    public int findTargetSumWays(int[] nums, int S) {
        ArrayList<Integer> ret = new ArrayList<Integer>();
        
        ret.add(0);
        
        helper(nums, 0, 0, S, ret);
        
        return ret.get(0);
    }
    
    
    private void helper(int[] nums, int index, int sum, int target, ArrayList<Integer> ret){
        if(index == nums.length){
            if(sum == target){
                ret.set(0, ret.get(0) + 1);
                return;
            }
            else{
                return;
            }
        }
        
        int positive = sum + nums[index];
        helper(nums, index + 1, positive, target, ret);
        
        int negative = sum - nums[index];
        helper(nums, index + 1, negative, target, ret);
        
    }
}