// Last updated: 2/23/2026, 6:46:30 PM
public class Solution {
    public int findMinDifference(List<String> timePoints) {
        int min = Integer.MAX_VALUE;
        
        Collections.sort(timePoints, new Comparator<String>(){
            public int compare(String t1, String t2){
                return convertToMinutes(t1) - convertToMinutes(t2);
            }
        });
        
        String first = timePoints.get(0);
        String last = timePoints.get(timePoints.size() - 1);
        
        min = convertToMinutes(first) - convertToMinutes("00:00") + convertToMinutes("24:00") - convertToMinutes(last);
        
        for(int i = 1; i < timePoints.size(); i++){
            String curr = timePoints.get(i);
            String prev = timePoints.get(i - 1);
            int diff = convertToMinutes(curr) - convertToMinutes(prev);
            min = Math.min(diff, min);
        }
        
        return min;
    }
    
    
    private int convertToMinutes(String time){
        String[] times = time.split(":");
        
        return 60 * Integer.parseInt(times[0]) + Integer.parseInt(times[1]);
    }
}