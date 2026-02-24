// Last updated: 2/23/2026, 6:45:06 PM
class Solution {
    public int largestIsland(int[][] grid) {
        int index = 1;
        Map<Integer, Integer> areaMap = new HashMap<>();
        for(int i=0; i<grid.length; i++) {
            for(int j=0; j<grid[0].length; j++) {
                if(grid[i][j]==1) {
                    index++;
                    areaMap.put(index, getArea(grid, i, j, index));
                }
            }
        }
        int max = 0;
        if(areaMap.size()==1 && areaMap.get(2)==grid.length*grid[0].length) {
            return grid.length*grid[0].length;
        }
        for(int i=0; i<grid.length; i++) {
            for(int j=0; j<grid[0].length; j++) {
                if(grid[i][j] == 0) {
                    int res = 1;
                    Set<Integer> neighbours = new HashSet<>();
                    if(i-1>=0 && grid[i-1][j]!=0) {
                        res += areaMap.get(grid[i-1][j]); 
                        neighbours.add(grid[i-1][j]);
                    }
                    if(i+1<grid.length && grid[i+1][j]!=0 && !neighbours.contains(grid[i+1][j])) {
                        res += areaMap.get(grid[i+1][j]);
                        neighbours.add(grid[i+1][j]);
                    }
                    if(j-1>=0 && grid[i][j-1]!=0 && !neighbours.contains(grid[i][j-1])) {
                        res += areaMap.get(grid[i][j-1]);
                        neighbours.add(grid[i][j-1]);
                    }
                    if(j+1<grid[0].length && grid[i][j+1]!=0 && !neighbours.contains(grid[i][j+1])) {
                        res += areaMap.get(grid[i][j+1]);
                        neighbours.add(grid[i][j+1]);
                    }
                    max = Math.max(res, max);
                }
            }
        }
        return max;
    }
    
    private int getArea(int[][] grid, int i, int j, int index) {
        int area = 1 ;
        grid[i][j] = index;
        if(i-1>=0 && grid[i-1][j]==1) {
            area += getArea(grid, i-1, j, index);
        }
        if(i+1<grid.length && grid[i+1][j]==1) {
            area += getArea(grid, i+1, j, index);
        }
        if(j-1>=0 && grid[i][j-1]==1) {
            area += getArea(grid, i, j-1, index);
        }
        if(j+1<grid[0].length && grid[i][j+1]==1) {
            area += getArea(grid, i, j+1, index);
        }
        return area;
    }
}