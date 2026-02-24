// Last updated: 2/23/2026, 6:44:27 PM
/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
};
*/

class Solution {
    public Node lowestCommonAncestor(Node p, Node q) {
        Node node1 = p;
        Node node2 = q;
        while(node1!=node2) {
            node1 = node1.parent;
            node2 = node2.parent;
            if(node1==null)
                node1 = q;
            if(node2==null)
                node2 = p;
        }
        return node1;
    }
}


// 1,2,4,
// 4, 2, 1, 1
// 1, 4, 2, 1