// Last updated: 2/23/2026, 6:46:28 PM
public class Solution {
    public String reverseStr(String s, int k) {
        if(s == null || s.length() == 0 || k == 0 || k == 1) return s;
        
        char[] array = s.toCharArray();
        
        int index = 0;
        
        while(index < s.length()){
            int start = index;
            int end = Math.min(index + 2 * k - 1, s.length() - 1);
            reverse(start, end, array, k);
            index += 2 * k;
        }
        
        return new String(array);
    }
    
    private void reverse(int start, int end, char[] array, int k){
        if(end > start + k - 1){
            end = start + k - 1;
        }
        
        while(start < end){
            char temp = array[start];
            array[start] = array[end];
            array[end] = temp;
            start++;
            end--;
        }
    }
}