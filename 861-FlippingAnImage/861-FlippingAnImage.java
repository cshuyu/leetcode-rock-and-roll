// Last updated: 2/23/2026, 6:45:05 PM
class Solution {
    public int[][] flipAndInvertImage(int[][] A) {
        if(A==null)
            return null;
        int len = A.length;
        for(int[] row: A) {
            for(int i=0; i*2<len; i++) {
                if(row[i] == row[len-i-1]) {
                    row[i] ^= 1;
                    row[len-i-1] = row[i];
                }
            }    
        }
        return A;
    }
}