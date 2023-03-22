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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;
        ListNode head = null;
        ListNode node = null;
        ListNode prev = null;
        while(l1 != null && l2!= null){
            int sum = l1.val + l2.val + carry;
            carry = sum/10;
            node = new ListNode(sum%10, null);
            if(prev!=null){
                prev.next = node;
            }
            if(head == null){
                head = node;
            }   
            prev = node;
            l1 = l1.next;
            l2 = l2.next;
        }
         while( l2!= null){
            int sum = l2.val + carry;
            carry = sum/10;
            node = new ListNode(sum%10, null);
             prev.next = node;
            prev = node;
            l2 = l2.next;
        }
         while(l1 != null){
            int sum = l1.val + carry;
            carry = sum/10;
            node = new ListNode(sum%10, null);
             prev.next = node;
            prev = node;
            l1 = l1.next;
        }
        if(carry != 0){
            prev.next = new ListNode(carry, null);
        }
        return head;
    }
}