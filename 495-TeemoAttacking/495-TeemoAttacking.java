// Last updated: 2/23/2026, 6:46:50 PM
public class Solution {
    public int findPoisonedDuration(int[] timeSeries, int duration) {
        if(duration <= 0 || timeSeries == null || timeSeries.length == 0) return 0;
        
        int count = 0;
        int end = 0;
        int prev = -1;
        
        for(int start : timeSeries){
            if(start >= end){
                count += duration;
                end = start + duration;
                prev = start;
            }
            else{
               count += start - prev;
               end = start + duration;
               prev = start;
            }
        }
        return count;
    }
}