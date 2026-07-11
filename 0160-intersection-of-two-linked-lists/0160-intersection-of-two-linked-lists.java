/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public int sizeLL(ListNode head){
        int count = 0;

        ListNode ptr = head;

        while(ptr!=null){
            count++;
            ptr = ptr.next;
        }
        return count;
    }
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if(headA == null || headB == null){
            return null;
        }
        int size1 = sizeLL(headA);
        int size2 = sizeLL(headB);

        int diff = size1 - size2;

        ListNode ptr1 = headA;
        ListNode ptr2 = headB;

        if(diff>0){
            while(diff>0){
                ptr1 = ptr1.next;
                diff--;
            }
          
        } else{
                while(diff<0){
                    ptr2 = ptr2.next;
                    diff++;
                }
        }

        while(ptr1!=ptr2){
            ptr1 = ptr1.next;
            ptr2 = ptr2.next;

        }
        return ptr1;
    }
}