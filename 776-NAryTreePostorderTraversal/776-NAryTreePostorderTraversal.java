// Last updated: 2/23/2026, 6:45:20 PM
/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    public List<Integer> postorder(Node root) {
        Stack<Node> stack = new Stack<>();
        List<Integer> reversedRs = new ArrayList<>();
        if (root == null) {
            return reversedRs;
        }
        stack.push(root);
        while(!stack.isEmpty()) {
            Node node = stack.pop();
            reversedRs.add(node.val);
            for(Node child : node.children) {
                stack.push(child);
            }
        }
        Collections.reverse(reversedRs);
        return reversedRs;
        
    }
}