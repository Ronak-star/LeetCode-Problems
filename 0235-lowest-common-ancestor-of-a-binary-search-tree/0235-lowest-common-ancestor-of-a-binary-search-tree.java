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
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root == null){
            return null;
        }

        TreeNode temp = root;

        while(temp!=null){
            if(temp.val > p.val && temp.val > q.val){
                  temp = temp.left;
            }else if (temp.val < p.val && temp.val < q.val){

            temp = temp.right;
            }else{
                break;
            }
        }
        return temp;
    }
}