// Last updated: 2/23/2026, 6:47:08 PM
public class Solution {
    public boolean circularArrayLoop(int[] nums) {
       if(nums == null || nums.length <= 1){
           return false;
       }
       
       boolean forward = nums[0] > 0 ? true: false;
       
       int size = nums.length;
       
       int count = 1;
       
       for(int i = 0; i < nums.length; i++){
           int source = i;
           int index = i;
           
           while(nums[index] != 0){
              int next = (index + nums[index]) % size ;
              
              boolean nextForward = next >= index ? true : false;
              
              if(next < 0){
                  next = next + size;
              }
              
              //find the loop
              if(next == source && count > 1){
                  return true;
              }
              
              //same direction
              if(nextForward == forward){
                  nums[index] = 0; // set to visited
                  count++;         //increase the count
                  index = next;
              }
              else{
                  nums[index] = 0;
                  forward = nextForward;
                  count = 1;
                  source = index;
                  index = next;
              }
           }
       }
       
       return false;
    }
}