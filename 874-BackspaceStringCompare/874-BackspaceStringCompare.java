// Last updated: 2/23/2026, 6:45:02 PM
class Solution {
    public boolean backspaceCompare(String s, String t) {
        int i=s.length()-1, j=t.length()-1;
        int sCount = 0, tCount = 0;
        while(true) {
            // Start to collect backspace for s
            while(i>=0 && s.charAt(i) == '#') {
                i--;
                sCount++;
            }
            // Start to delete
            while(i>=0 && sCount > 0 && s.charAt(i) != '#') {
                sCount--;
                i--;
            }
            if (i>=0 && s.charAt(i) == '#') continue;
            // Now 1) i<0 or s.charAt(i) != '#'

            // Start to collect backspace for t
            while(j>=0 && t.charAt(j) == '#') {
                j--;
                tCount++;
            }
            // Start to delete
            while(j>=0 && tCount > 0 && t.charAt(j) != '#') {
                tCount--;
                j--;
            }
            if (j>=0 && t.charAt(j) == '#') continue;

            if (i<0 && j<0) return true;
            else if(i <0) return false;
            else if(j<0) return false;
            else if (s.charAt(i) != t.charAt(j)) return false;
            i--;
            j--;
        }
    }
}