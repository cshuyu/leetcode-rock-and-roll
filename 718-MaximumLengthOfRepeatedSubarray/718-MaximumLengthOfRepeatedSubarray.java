// Last updated: 2/23/2026, 6:45:56 PM
class Solution {
    public int findLength(int[] nums1, int[] nums2) {
        // array[i][j] means the max length for array 
        // nums1[:i] and nums2[:j], and the longest str
        // ends with nums1[i] and nums2[j]

        // array[i][j]:
        //   case1: array[i-1][j-1] and nums1[i] == nums2[j]
        //   case2: array[i][j-1] and 
        int len1 = nums1.length;
        int len2 = nums2.length;
        int[][] arr = new int[len1][len2];
        int max = 0;
        for(int i=0; i<len1; i++) {
            arr[i][0] = nums1[i] == nums2[0] ? 1 : 0;
            max = Math.max(arr[i][0], max);
        }
        for(int i=0; i<len2; i++) {
            arr[0][i] = nums1[0] == nums2[i] ? 1 : 0;
            max = Math.max(arr[0][i], max);
        }
        for(int i=1; i<len1; i++) {
            for(int j=1; j<len2; j++) {
                if (nums1[i] == nums2[j]) {
                    arr[i][j] = arr[i-1][j-1] + 1;
                    max = Math.max(max, arr[i][j]);
                } 
            }
        }
        return max;
    }
}