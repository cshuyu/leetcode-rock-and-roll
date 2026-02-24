// Last updated: 2/23/2026, 6:45:17 PM
class Solution {
    public int numJewelsInStones(String J, String S) {
        Set<Character> jSet = new HashSet<>();
        for(int i=0; i<J.length(); i++) {
            jSet.add(J.charAt(i));
        }
        int res = 0;
        for(int j=0; j<S.length(); j++) {
            if(jSet.contains(S.charAt(j)))
                res++;
        }
        return res;
    }
}