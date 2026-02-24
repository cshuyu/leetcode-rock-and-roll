// Last updated: 2/23/2026, 6:46:57 PM
public class Solution {
    public int[] findPermutation(String s) {
       int size = s.length();
       
       int[] array = new int[size + 1];
       
       for(int i = 0; i < array.length; i++){
           array[i] = i + 1;
       }
       
       int index = 0;
       
       while(index < s.length()){
           if(s.charAt(index) == 'I'){
               index++;
           }
           else{
               int start = index;
               while(index < s.length() && s.charAt(index) == 'D'){
                   index++;
               }
               int end = index;
               
               while(start < end){
                   int temp = array[start];
                   array[start] = array[end];
                   array[end] = temp;
                   start++;
                   end--;
               }
           }
       }
       
       return array;
    }
}