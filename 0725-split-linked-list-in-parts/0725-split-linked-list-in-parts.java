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
class Solution {
    public ListNode[] splitListToParts(ListNode head, int k) {
        ListNode[] result = new ListNode[k];
        int size = 0;
        ListNode current = head;
        while(current != null){
            size++;
            current = current.next;
        }
        int splitSize = size / k;
        int numRemainigParts = size % k;
        current = head;
        for(int i=0; i<k; i++){
            ListNode newPart = new ListNode(0);
            ListNode tail = newPart;
            int currentSize = splitSize;
            if(numRemainigParts  > 0){
                currentSize++;
              numRemainigParts --;
            }
            int j = 0;
            while(j< currentSize){
                tail.next = new ListNode(current.val);
                tail = tail.next;
                j++;
                current = current.next;
            }
            result[i] = newPart.next;
        }
        return result;
    }
}