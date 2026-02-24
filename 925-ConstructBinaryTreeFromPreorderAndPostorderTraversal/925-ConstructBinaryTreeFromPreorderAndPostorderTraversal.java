// Last updated: 2/23/2026, 6:44:59 PM
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    //    1
    // . 2 .  3
    // 4 . 5 6  7
    // pre   1 2 4 5 3 6 7
    // post  4 5 2 6 7 3 1
    
    // .   1
    // . 2
    // .3 .4
    // pre . 1 2 3 4
    // post .3 4 2 1
    
    // .    1
    //         2
    //        3  4
    // pre   1 2 3 4
    // post .3 4 2 1
    public TreeNode constructFromPrePost(int[] pre, int[] post) {
        return build(pre, 0, pre.length-1, post, 0, post.length-1);
    }
    
    TreeNode build(int[] pre, int preBeg, int preEnd, int[] post, int postBeg, int postEnd) {
        if (preBeg > preEnd) return null;
        TreeNode node = new TreeNode(pre[preBeg]);
        if (preBeg == preEnd) return node;
        
        int leftChildVal = pre[preBeg+1];
        int rightChildVal = post[postEnd-1];
        
        if (leftChildVal == rightChildVal) {
            node.left = build(pre, preBeg+1, preEnd, post, postBeg, postEnd-1);
        } else {
            int i = 1;
            for(i=1; i+preBeg<=preEnd; i++)
                if (pre[i+preBeg] == rightChildVal)
                    break;
            int cnt = i - 1;
            node.left = build(pre, preBeg+1, preBeg+cnt, post, postBeg, postBeg+cnt-1);
            node.right = build(pre, preBeg+i, preEnd, post, postBeg+cnt, postEnd - 1);
        }
        
        return node;   
    }
}