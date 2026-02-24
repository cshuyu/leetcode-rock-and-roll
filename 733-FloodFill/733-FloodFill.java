// Last updated: 2/23/2026, 6:45:52 PM
class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        if (image == null || image.length == 0 || image[0].length == 0) return image;
        int colCnt = image[0].length;
        int rowCnt = image.length;
        dfs(image, sr, sc, color, new boolean[colCnt * rowCnt]);
        return image;
    }

    private void dfs(int[][] image, int r, int c, int color, boolean[] visited) {
        int colCnt = image[0].length;
        int rowCnt = image.length;
        visited[r*colCnt + c] = true;
        int[][] dirs = {{-1,0}, {1,0}, {0,-1}, {0, 1}};
        for(int[] dir : dirs) {
            int newR = r + dir[0];
            int newC = c + dir[1];
            if (newR < 0 || newR >= rowCnt) continue;
            if (newC < 0 || newC >= colCnt) continue;
            int idx = newR * colCnt + newC;
            if (visited[idx]) continue;
            if (image[newR][newC] != image[r][c])
                continue;
            dfs(image, newR, newC, color, visited);
        }
        image[r][c] = color;
    }
}