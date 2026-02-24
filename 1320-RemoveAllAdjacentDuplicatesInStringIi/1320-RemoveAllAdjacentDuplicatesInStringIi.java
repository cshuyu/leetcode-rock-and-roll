// Last updated: 2/23/2026, 6:44:41 PM
class Solution {
    public String removeDuplicates(String s, int k) {
        StringBuilder sb = new StringBuilder();
        Stack<Integer> stack = new Stack<>();
        int cnt = 0;
        int len = 0;
        char[] chars = s.toCharArray();
        for(char c : chars) {
            if (len > 0 && sb.charAt(len-1) == c) {
                cnt++;
            } else {
                stack.push(cnt);
                cnt = 1;
            }
            
            if (k == cnt) {
                len -= k - 1;
                cnt = stack.pop();
            } else {
                sb.insert(len++, c);
            }
        }
        return sb.substring(0, len);
    }
}