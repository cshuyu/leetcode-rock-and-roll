// Last updated: 2/23/2026, 6:47:01 PM
public class Solution {
    public int findRadius(int[] houses, int[] heaters) {
        Arrays.sort(heaters);

        int min = 0;

        for(int i = 0; i < houses.length; i++){
          int curr = houses[i];
          int radius = determineRadius(curr, heaters);
          min = Math.max(min, radius);
        }

        return min;

    }

    private int determineRadius(int curr, int[] heaters){
        int l = 0;
        int r = heaters.length - 1;

        while(l < r){
          int mid = l + (r - l) / 2;
          if(curr == heaters[mid]){
            return 0;
          }
          else if(curr > heaters[mid]){
            l = mid + 1;
          }
          else{
            r = mid;
          }
        }

        if(l == 0) return Math.abs(curr - heaters[l]);

        return Math.min(Math.abs(curr - heaters[l]), Math.abs(curr - heaters[l - 1]));
        
    }
}