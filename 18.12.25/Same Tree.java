/**
 * Definition for a binary tree node. 
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        // Both nodes are null - they are the same
        if (p == null && q == null) {
            return true;
        }
        
        // One is null and the other is not - they are different
        if (p == null || q == null) {
            return false;
        }
        
        // Both nodes exist - check if values are equal
        // and recursively check left and right subtrees
        return (p.val == q.val) 
            && isSameTree(p.left, q.left) 
            && isSameTree(p.right, q.right);
    }
}
