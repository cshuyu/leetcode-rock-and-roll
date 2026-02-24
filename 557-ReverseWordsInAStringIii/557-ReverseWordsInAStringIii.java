// Last updated: 2/23/2026, 6:46:20 PM
class Solution {
    public String reverseWords(String s) {
        StringBuilder res = new StringBuilder();
        StringBuilder word = new StringBuilder();
        for(int i=0; i<s.length(); i++) {
            if(s.charAt(i) != ' ')
                word.append(s.charAt(i));
            else {
                if (word.length() > 0) {
                    res.append(reverse(word.toString())+" ");
                    word = new StringBuilder();
                } else {
                    res.append(" ");
                }
            }
        }
        
        res.append(reverse(word.toString()));
        
        return res.toString();
    }
    
    private String reverse(String s) {
        char[] sarray = s.toCharArray();  
        int i=0, j=sarray.length-1;
        while(i<j) {
            char tmp = sarray[i];
            sarray[i] = sarray[j];
            sarray[j] = tmp;
            i++;
            j--;
        }
        return String.valueOf(sarray);
    }
}