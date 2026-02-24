// Last updated: 2/23/2026, 6:45:08 PM
class Solution {
    public int[] numberOfLines(int[] widths, String s) {
        int rowCnt = 1;
        int val = 0;
        int rest = 100;
        int[] res = new int[2];
        for(int i=0; i<s.length(); i++) {
            char c = s.charAt(i);
            int width = widths[c-'a'];
            rest = rest-width;                
            if(rest>=0) {
                val+=width;   
            }
            else {
                rest = 100-width;
                val = width;
                rowCnt++;
            } 
        }
        res[0] = rowCnt;
        res[1] = val;
        return res;        
    }
}