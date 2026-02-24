// Last updated: 2/23/2026, 6:45:54 PM
class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        int left = 0;
        int right = letters.length-1;
        while(left<right-1) {
            int mid = left + (right-left)/2;
            if(letters[mid]<=target) {
                left = mid + 1;  
            }
            if(letters[mid]>target) {
                right = mid;
            }
        }
        if(letters[left]>target) {
            return letters[left];
        }
        else if(letters[right]>target)
            return letters[right];
        else
            return letters[0];
    }
}