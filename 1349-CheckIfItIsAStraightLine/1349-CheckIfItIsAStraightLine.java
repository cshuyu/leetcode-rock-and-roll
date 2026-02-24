// Last updated: 2/23/2026, 6:44:40 PM
class Solution {
    public boolean checkStraightLine(int[][] coordinates) {
        if(coordinates.length<=2)
            return true;
        
        for(int i=1; i<coordinates.length-1; i++) {
            int x1 = coordinates[0][0];
            int x2 = coordinates[i][0];
            int x3 = coordinates[i+1][0];
            int y1 = coordinates[0][1];
            int y2 = coordinates[i][1];
            int y3 = coordinates[i+1][1];
            
            if((y2-y1)*(x3-x2) == (x2-x1)*(y3-y2))
                continue;
            else
                return false;
        }
        return true;
    }
}