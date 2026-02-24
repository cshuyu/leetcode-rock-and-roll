// Last updated: 2/23/2026, 6:46:37 PM
class Solution {
    int count = 0;
    public int countArrangement(int n) {
        int[] nArray = new int[n];
        for(int i=0; i<n; i++) {
            nArray[i] = i+1;
        }
        dfs(nArray, 0);
        return count;
    }
    
    private void dfs(int[] nArray, int start) {
        if(start==nArray.length) {
            count++;
        }
        for(int i=start; i<nArray.length; i++) {
            if(nArray[i]%(start+1)==0 || (start+1)%nArray[i]==0) {
                swap(nArray, start, i);
                dfs(nArray, start+1);
                swap(nArray, start, i);    
            }
        }
    }
    
    public void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }  
}