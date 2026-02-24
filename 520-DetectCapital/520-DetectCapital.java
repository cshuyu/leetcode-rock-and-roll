// Last updated: 2/23/2026, 6:46:37 PM
public class Solution {
    public boolean detectCapitalUse(String word) {
        if(word == null) return false;
        if(word.length() == 0) return true;
        
        String upper = new String(word).toUpperCase();
        String lower = new String(word).toLowerCase();
        String cap = word.substring(0,1).toUpperCase() + word.substring(1).toLowerCase();
        
        return word.equals(upper) || word.equals(lower) || word.equals(cap);
    }
}