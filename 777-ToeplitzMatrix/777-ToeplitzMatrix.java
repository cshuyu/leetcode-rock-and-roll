// Last updated: 2/23/2026, 6:45:17 PM
class Solution {
    public boolean isToeplitzMatrix(int[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length==0) return false;
        int colSize = matrix[0].length;
        int rowSize = matrix.length;

        // Iterate the first row.
        for(int col=0; col<colSize; col++) {
            int v = matrix[0][col];
            for(int row = 1; row < rowSize && col+row < colSize; row++) {
                if (matrix[row][col+row] != v)
                    return false;
            }
        }
        // Iterate the first col
        for (int row=1; row<rowSize; row++) {
            int v = matrix[row][0];
            for (int col=1; col<colSize && row+col < rowSize; col++) {
                if (matrix[row+col][col] != v) {
                    return false;
                }
            }
        }
        return true;
    }
}