// Last updated: 2/23/2026, 6:44:57 PM
class Solution {
    int[] prefixSum;
    int totalSum;
    public Solution(int[] w) {
        prefixSum = new int[w.length];
        prefixSum[0] = 0;
        for(int i=1; i<w.length; i++) {
            prefixSum[i] = prefixSum[i-1] + w[i-1];
        }
        totalSum = prefixSum[w.length-1] + w[w.length-1];
    }
    
    public int pickIndex() {
        double chosenVal = totalSum * Math.random();
        int i = 0;
        int j = prefixSum.length-1;
        while(i<j) {
            int mid = i+(j-i)/2;
            if(prefixSum[mid+1]<=chosenVal)
                i = mid+1;
            else if(prefixSum[mid]<=chosenVal) {
                return mid;    
            }
            else {
                j = mid-1;
            }
        }
        if(prefixSum[j]<=chosenVal) {
            return j;
        }
        else
            return i;    
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(w);
 * int param_1 = obj.pickIndex();
 */