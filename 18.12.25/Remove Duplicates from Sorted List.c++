/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        // Handle empty list or single node
        if (head == nullptr || head->next == nullptr) {
            return head;
        }
        
        // Start from the head
        ListNode* current = head;
        
        // Traverse the list
        while (current != nullptr && current->next != nullptr) {
            // If current node's value equals next node's value
            if (current->val == current->next->val) {
                // Skip the duplicate node
                ListNode* duplicate = current->next;
                current->next = current->next->next;
                delete duplicate; // Optional: free memory
            } else {
                // Move to next node only if no duplicate found
                current = current->next;
            }
        }
        
        return head;
    }
};
