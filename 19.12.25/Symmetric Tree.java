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
    public boolean isSymmetric(TreeNode root) {
        if (root == null) {
            return true;
        }
        return isMirror(root.left, root.right);
    }
    
    private boolean isMirror(TreeNode left, TreeNode right) {
        // Both nodes are null - symmetric
        if (left == null && right == null) {
            return true;
        }
        
        // One is null and the other is not - not symmetric
        if (left == null || right == null) {
            return false;
        }
        
        // Check if: 
        // 1. Current values are equal
        // 2. Left's left subtree mirrors Right's right subtree
        // 3. Left's right subtree mirrors Right's left subtree
        return (left. val == right.val)
            && isMirror(left. left, right.right)
            && isMirror(left. right, right.left);
    }
}
