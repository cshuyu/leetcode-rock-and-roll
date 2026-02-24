// Last updated: 2/23/2026, 6:45:23 PM
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
    public List<Integer> preorder(Node root) {
        if (root == null) return new ArrayList<>();
        Stack<Node> stack = new Stack<>();
        stack.push(root);
        List<Integer> rs = new ArrayList<>();
        while(!stack.isEmpty()) {
            Node node = stack.pop();
            if (node.children != null) {
                for(int i=node.children.size()-1; i>=0; i--) {
                    if (node.children.get(i) != null)
                        stack.push(node.children.get(i));
                }
            }
            rs.add(node.val);
        }
        return rs;
    }
}