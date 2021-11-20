/*
 * @lc app=leetcode.cn id=2074 lang=cpp
 *
 * [2074] 反转偶数长度组的节点
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
class Solution {
public:
    ListNode* reverseEvenLengthGroups(ListNode* head) {
        ListNode* rec = head;
        int cnt = 1;
        int cur_group = 1;
        ListNode* last = nullptr;
        stack<ListNode*> s;
        while(head){
            if(cnt == 1 && ((cur_group & 0x01) == 1)) {
                last = head;
            }
            s.push(head);
            head = head->next;
            if((cnt == 1 || !head)){
                if((s.size() + 1) & 0x01){
                    //ListNode* next = head;
                    while(!s.empty()) {
                        last->next = s.top();
                        s.pop();
                        last = last->next;
                    }
                        last ->next = head;
                }else{
                    while(!s.empty()){
                        s.pop();
                    }
                }
            }

            if(cnt == 1){
                cur_group += 1;
                cnt = cur_group;
            } else{
                cnt -= 1;
            }
        }
        return rec;
    }
};
// @lc code=end

