// Last updated: 2/23/2026, 6:45:13 PM
class Solution {
    public boolean isBipartite(int[][] graph) {
        Queue<Integer> nodeQueue = new LinkedList<Integer>();
        int[] visited = new int[graph.length];
        for(int i=0; i<graph.length; i++) {
            if(visited[i]!=0)
                continue;
            visited[i] = 1;
            nodeQueue.add(i);
            while(!nodeQueue.isEmpty()) {
                int node = nodeQueue.poll();
                for(int neighbor: graph[node]) {
                    if(visited[neighbor]==visited[node]) {
                        return false;    
                    }
                    if(visited[neighbor]==0) {
                        visited[neighbor] = visited[node]*(-1);
                        nodeQueue.add(neighbor);
                    }
                }
            }
        }
        return true;
    }
}