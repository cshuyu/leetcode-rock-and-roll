// Last updated: 2/23/2026, 6:47:18 PM
public class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> rs = new ArrayList<Integer>();
        for(int i=0; i<nums.length; i++){
            int num = Math.abs(nums[i]);
            int idx = num-1;
            if(nums[idx] < 0)
                rs.add(num);
            nums[idx] = -nums[idx];
        }
        return rs;
    }
}