// Last updated: 2/23/2026, 6:46:04 PM
class Solution {
    public int repeatedStringMatch(String A, String B) {
        char[] a = A.toCharArray();
        char[] b = B.toCharArray();
        for(int i=0; i<a.length; i++) {
            if (b[0] == a[i]) {
                int cnt = 1;
                int len = Math.min(b.length, a.length-i);
                boolean good = true;
                for(int j=i; j<i+len; j++) {
                    if (a[j] != b[j-i]){
                        good = false;
                        break;
                    }
                }
                if (good) {
                    // System.out.println("-- "+i+" "+len);
                    String bRes = B.substring(len);
                    if(bRes.isEmpty()) return 1;
                    StringBuilder sb = new StringBuilder();
                    while(sb.length() < bRes.length()) {
                        sb.append(A);
                        cnt++;
                    }
                    if (sb.toString().startsWith(bRes)) {
                        return cnt;
                    }
                }
            }    
        }
        return -1;
    }
}