// Last updated: 2/23/2026, 6:46:06 PM
class Solution {
    int cmax = 0;
    int cmin = 0;
    public boolean checkValidString(String s) {
        for(int i=0; i<s.length(); i++) {
            if(s.charAt(i)=='(') {
                cmax++;
                cmin++;
            }
            else if(s.charAt(i)==')') {
                cmax--;
                cmin--;
            }
            else {
                cmax++;
                cmin--;
            }
            if(cmax<0)
                return false;
            if(cmin<0)
                cmin=0;
        }
        return cmin==0;
    }  
}



