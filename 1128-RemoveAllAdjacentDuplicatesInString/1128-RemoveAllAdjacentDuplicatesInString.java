// Last updated: 2/23/2026, 6:44:48 PM
class Solution {
    public String removeDuplicates(String S) {
        StringBuilder sb = new StringBuilder();
        int len = 0;
        for(char c : S.toCharArray()) {
            if(len>0 && c == sb.charAt(len-1)) {
                sb.deleteCharAt(--len);
            } else {
                sb.append(c);
                len = sb.length();
            }
        }
        return sb.toString();
    }
}