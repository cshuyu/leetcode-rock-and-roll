// Last updated: 2/23/2026, 6:46:54 PM
public class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        if(nums == null || nums.length == 0) return 0;
        
        int prevEndIndex = -1;
        int prevCount = 0;
        int currStart = -1;
        int currEnd = -1;
        int index = 0;
        int max = 0;
        
        while(index < nums.length){
            if(nums[index] == 0){
                while(index < nums.length && nums[index] == 0){
                    index++;
                }
            }
            else{
                currStart = index;
                while(index < nums.length && nums[index] == 1){
                    index++;
                }
                currEnd = index - 1;
                
                int currLength = currEnd - currStart + 1;
                if(currStart - prevEndIndex == 2){
                    currLength += 1 + prevCount;
                }
                else if(currStart - prevEndIndex > 2) {
                     currLength += 1;
                }
                else{
                    if(currLength != nums.length){
                        currLength++;
                    }
                }
                
                max = Math.max(max, currLength);
                prevEndIndex = currEnd;
                prevCount =  currEnd - currStart + 1;
                
            }
        }
        
        if(currStart == -1){
            return 1;
        }
        
        return max;
    }
}