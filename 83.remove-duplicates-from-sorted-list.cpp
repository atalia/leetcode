/*
 * @lc app=leetcode id=83 lang=cpp
 *
 * [83] Remove Duplicates from Sorted List
 */

// @lc code=start
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
#include<iostream>


struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
  };


class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* cur = head;
        
        while(cur && cur->next){
            if(cur->val == cur->next->val){
                cur->next = cur->next->next;
            }else{
                cur = cur->next;
            }
        }
        if(cur){
            cur->next = nullptr;
        }
        
        return head;
    }
};

int main(){
    ListNode* root = new ListNode(1);
    root->next = new ListNode(1);
    root->next->next = new ListNode(2);
    root->next->next->next = new ListNode(3);
    root->next->next->next->next = new ListNode(3);

    ListNode* res = Solution().deleteDuplicates(root);
    while(res){
        std::cout << res->val << " ";
        res = res->next;
    }
}
// @lc code=end

