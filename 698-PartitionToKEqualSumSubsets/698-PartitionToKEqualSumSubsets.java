// Last updated: 2/23/2026, 6:46:01 PM
class Solution {
    public boolean canPartitionKSubsets(int[] nums, int k) {
        int length = nums.length;
        char[] used = new char[length];
        int totalSum = 0;
        for(int i=0; i<length; i++) {
            used[i] = '0';
            totalSum += nums[i];
        }
        if(totalSum % k != 0 || length<k)
            return false;
        int targetSum = totalSum/k;
        
        // Memorize the ans using taken element's string as key
        HashMap<String, Boolean> memo = new HashMap<>();
        
        return dfs(nums, 0, 0, targetSum, k, used, memo);
    }
    
    private boolean dfs(int[] nums, int index, int currSum, int targetSum, int left, char[] used, HashMap<String, Boolean> memo) {
        if(left==1) {
            return true;   
        }
        if(currSum>targetSum)
            return false;
        
        String takenStr = new String(used);
        
        if(memo.containsKey(takenStr))
            return memo.get(takenStr);    
        
        if(currSum==targetSum) {
            boolean ans = dfs(nums, 0, 0, targetSum, left-1, used, memo);
            memo.put(takenStr, ans);
            return ans;
        }
        
        for(int i=index; i<nums.length; i++) {
            if(used[i] == '1')
                continue;
            used[i] = '1';
            if(dfs(nums, i+1, currSum+nums[i], targetSum, left, used, memo))
                return true;
            used[i] = '0';
        }
        return false;
    }
}