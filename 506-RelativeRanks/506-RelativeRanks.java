// Last updated: 2/23/2026, 6:46:44 PM
public class Solution {
    public String[] findRelativeRanks(int[] nums) {
        if(nums == null || nums.length == 0) return new String[0];
        
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>(nums.length, new Comparator<Integer>(){
            public int compare(Integer n1, Integer n2){
                return n2 - n1;
            }
        });
        
        for(int i = 0; i < nums.length; i++){
            map.put(nums[i], i);
            pq.add(nums[i]);
        }
        
        String[] ret = new String[nums.length];
        
        int rank = 1;
        
        while(!pq.isEmpty()){
            int score = pq.remove();
            int index = map.get(score);
            switch(rank){
                case 1:
                    ret[index] = "Gold Medal"; break;
                case 2:
                    ret[index] = "Silver Medal"; break;
                case 3:
                    ret[index] = "Bronze Medal"; break;
                default:
                    ret[index] = rank + ""; break;
            }
            rank++;
        }
        
        return ret;
    }
}