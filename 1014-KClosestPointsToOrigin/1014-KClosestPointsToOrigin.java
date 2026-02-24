// Last updated: 2/23/2026, 6:44:51 PM
class Solution {
    public int[][] kClosest(int[][] points, int k) {
        int[][] res = new int[k][2];
        if(points==null || points.length==0 || points.length<k)
            return res;
        quickSelect(points, 0 , points.length-1, k-1);
        for(int i=0; i<k; i++) {
            res[i][0] = points[i][0];
            res[i][1] = points[i][1];
        }
        return res;
    }
    
    private void quickSelect(int[][] points, int start, int end, int idx) {
        int pivot = partition(points, start, end);
        if(pivot==idx)
            return;
        else if(pivot<idx)
            quickSelect(points, pivot+1, end, idx);
        else
            quickSelect(points, start, pivot-1, idx);
    }
    
    private int partition(int[][] points, int start, int end) {
        int pivotVal = dist(points, end);
        int i = start;
        int j = end-1;
        while(i<=j) {
            if(dist(points, i) < pivotVal) {
                i++;
            }
            else if(dist(points, j) >= pivotVal) {
                j--;
            }
            else {
                swap(points, i++, j--);
            }
        }
        swap(points, i, end);
        return i;
    }
    
    private int dist(int[][] points, int i) {
        return points[i][0]*points[i][0] + points[i][1]*points[i][1];
    }
    
    private void swap(int[][] points, int i, int j) {
        int tmpX = points[i][0];
        int tmpY = points[i][1];
        points[i][0] = points[j][0];
        points[i][1] = points[j][1];
        points[j][0] = tmpX;
        points[j][1] = tmpY;
    }
}