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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode cur = new ListNode();
        ListNode head = cur;
        if(list1 == null) return list2;
        if(list2 == null) return list1;
        while(true){
            if(list1.val > list2.val){
                cur.val = list2.val;
                list2 = list2.next;
                 cur.next = new ListNode();
            cur = cur.next;
                if(list2 == null) break;
            }else{
                cur.val = list1.val;
                list1 = list1.next;
                 cur.next = new ListNode();
            cur = cur.next;
                if(list1 == null) break;
            }
           
        }
                                    if(list1 != null) {

        while(true){
            cur.val = list1.val;
                list1 = list1.next;
                            if(list1 == null) break;
else         {
                cur.next = new ListNode();
    cur = cur.next;
             }

        }
                                    }
                    if(list2 != null) {

        while(true){
            cur.val = list2.val;
                list2 = list2.next;
            if(list2 == null) break;
            else{
            cur.next = new ListNode();
            cur = cur.next;
            }
        }
                    }
        return head;
    }
}