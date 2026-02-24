// Last updated: 2/23/2026, 6:46:09 PM
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<List<String>> printTree(TreeNode root) {
        List<List<String>> res = new ArrayList<>();
        int height = getHeight(root)-1;
        int col = (int)Math.pow(2, height+1)-1;

        for(int i=0; i<=height; i++) {
            List<String> rowString = new ArrayList<>();
            for(int j=0; j<col; j++) {
                rowString.add("");
            }
            res.add(rowString);
        }
        traverse(root, res, 0, (col-1)/2, height);
        return res;
    }

    private int getHeight(TreeNode root) {
        if(root==null)
            return 0;
        return 1+Math.max(getHeight(root.left), getHeight(root.right));
    }

    private void traverse(TreeNode node, List<List<String>> res, int row, int col, int height) {
        if(node==null)
            return;
        res.get(row).set(col, String.valueOf(node.val));
        traverse(node.left, res, row+1, col-(int)Math.pow(2, height-row-1), height);
        traverse(node.right, res, row+1, col+(int)Math.pow(2, height-row-1), height);
    }
}

