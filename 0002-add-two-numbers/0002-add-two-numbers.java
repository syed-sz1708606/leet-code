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
        
        ListNode dummy = new ListNode(0); 
        ListNode new_list = dummy; 
        
        int carry = 0; 
        
        while(l1 != null || l2 != null){
            
            int v1 = (l1 != null) ? l1.val : 0; 
            int v2 = (l2 != null) ? l2.val : 0;
            
            int sum = v1 + v2 + carry; 
            int digit = sum % 10; 
            carry = sum / 10; 
       
            ListNode new_digit = new ListNode(digit); 
            new_list.next = new_digit; 
            
            if (l1 != null) l1 = l1.next; 
            if (l2 != null) l2 = l2.next; 
            new_list  = new_list .next; 
        }
        
        if(carry == 1){ 
        ListNode node = new ListNode(carry); 
        new_list.next = node;
        new_list  = new_list.next; 
        }
        
        return dummy.next; 
    }
}