// Last updated: 2/23/2026, 6:47:14 PM
public class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> ret = new ArrayList<Integer>();
        
        if(nums == null || nums.length < 1){
            return ret;
        }
        
        for(int i = 0; i < nums.length; i++){
            while(nums[i] != i + 1){
                if(nums[i] == nums[nums[i] - 1]){
                    break;
                }
                else{
                    int temp = nums[i];
                    nums[i] = nums[nums[i] -1];
                    nums[temp -1] = temp;
                }
            }
        }
        
        for(int i = 0; i < nums.length; i++){
            if(nums[i] != i + 1){
                ret.add(i + 1);
            }
        }
        
        return ret;
    }
}