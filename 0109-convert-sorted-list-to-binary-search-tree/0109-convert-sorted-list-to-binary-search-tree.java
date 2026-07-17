/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
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
    public ListNode middleNode(ListNode head){

        if(head == null){
            return null;
        }

        ListNode fast = head;
        ListNode slow = head;
        ListNode pre = slow;

        while(fast!=null && fast.next!=null){
            pre = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
          pre.next = null;
        return slow;
    }
    public TreeNode sortedListToBST(ListNode head) {
        if(head == null){
            return null;
        }else if(head.next == null){
            TreeNode root = new TreeNode(head.val);
            return root;
        }

        ListNode mid = middleNode(head);

        TreeNode root = new TreeNode(mid.val);

        root.left = sortedListToBST( head) ;
        root.right = sortedListToBST(mid.next); 

        return root;
    }
}