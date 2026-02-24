// Last updated: 2/23/2026, 6:47:22 PM
class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        int[] count = new int[256];
        for(int i=0; i<p.length(); i++) {
            count[p.charAt(i)]++;
        }
        List<Integer> rs = new ArrayList<>();
        int pLength = p.length();
        int first = 0, last = 0;
        while(true) {
            // Find the longest period.
            last = Math.max(first, last);
            while (last < s.length() && (last- first < pLength) && count[s.charAt(last)] >0) {
                count[s.charAt(last++)]--;
            }
            // Not including the last
            if (last-first == pLength) {
                rs.add(first);
                count[s.charAt(first++)]++;
                continue;
            } else if (last == s.length()) {
                return rs;
            } 
            
            // no match
            if (first == last)
                first++;
            else
                count[s.charAt(first++)]++;
        }
    }
}