// Last updated: 2/23/2026, 6:46:56 PM
class Solution {
    public String licenseKeyFormatting(String S, int K) {
        StringBuilder sb = new StringBuilder();
        String s = S.toUpperCase();
        for(int i=s.length()-1; i>=0; i--) {
            if(s.charAt(i) != '-') {
                if(sb.length()%(K+1) == K)
                    sb.append("-");
                sb.append(s.charAt(i));
            }
            // else {
            //     if(sb.length()%(K+1) == K)
            //         sb.append(s.charAt(i));
            //     else
            //         sb.append("");
            // }    
        }
        return sb.reverse().toString();
    }
}