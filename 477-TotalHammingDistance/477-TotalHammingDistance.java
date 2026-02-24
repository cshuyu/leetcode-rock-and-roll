// Last updated: 2/23/2026, 6:46:59 PM
public class Solution {
    public int totalHammingDistance(int[] nums) {
        int count = 0;
        
        if(nums == null || nums.length <= 1){
            return 0;
        }
        
        int size = nums.length;
        
        for(int i = 0; i < 32; i++){
            int bitCount = 0;
            for(int j = 0; j < size; j++){
                int curr = nums[j];
                bitCount += ((curr >> i) & 1);
            }
            
            count += bitCount * (size - bitCount);
        }
        
        
        
        return count;
    }
}