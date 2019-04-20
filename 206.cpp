/*
206. Reverse Linked List
Reverse a singly linked list.
Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?
*/
#include <iostream>
#include <cctype>
#include <string>
#include <cstdlib>
#include <queue>
#include <sstream>
#include <algorithm>
using namespace std;
struct ListNode {
      int val;
      ListNode *next;
      ListNode(int x) : val(x), next(NULL) {}
    
};
//迭代版本
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if(head == NULL || head->next == NULL)
            return head;
        ListNode* pre = NULL;
        ListNode* cur = head;
        ListNode* tail = head->next;
        while(cur!=NULL)
        {
            tail = cur->next;
            cur->next = pre;
            pre = cur;
            cur = tail;
        }
        return pre;
    }
};
//递归版本
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if( head == NULL || head->next == NULL)
           return head;
        return reverseList(head,NULL);
    }
private:
    ListNode* reverseList(ListNode* head,ListNode* pre)
    {
        if(head == NULL)
            return pre;
        ListNode* tmp = head->next;
        head->next = pre;
        return reverseList(tmp,head);
    }
};
void trimLeftTrailingSpaces(string &input) {
    input.erase(input.begin(), find_if(input.begin(), input.end(), [](int ch) {
        return !isspace(ch);
    }));
}

void trimRightTrailingSpaces(string &input) {
    input.erase(find_if(input.rbegin(), input.rend(), [](int ch) {
        return !isspace(ch);
    }).base(), input.end());
}

vector<int> stringToIntegerVector(string input) {
    vector<int> output;
    trimLeftTrailingSpaces(input);
    trimRightTrailingSpaces(input);
    input = input.substr(1, input.length() - 2);
    stringstream ss;
    ss.str(input);
    string item;
    char delim = ',';
    while (getline(ss, item, delim)) {
        output.push_back(stoi(item));
    }
    return output;
}

ListNode* stringToListNode(string input) {
    // Generate list from the input
    vector<int> list = stringToIntegerVector(input);
    
    // Now convert that list into linked list
    ListNode* dummyRoot = new ListNode(0);
    ListNode* ptr = dummyRoot;
    for(int item : list) {
        ptr->next = new ListNode(item);
        ptr = ptr->next;
    }
    ptr = dummyRoot->next;
    delete dummyRoot;
    return ptr;
}

string listNodeToString(ListNode* node) {
    if (node == nullptr) {
        return "[]";
    }
    
    string result;
    while (node) {
        result += to_string(node->val) + ", ";
        node = node->next;
    }
    return "[" + result.substr(0, result.length() - 2) + "]";
}

int main() {
    string line;
    while (getline(cin, line)) {
        ListNode* head = stringToListNode(line);
        
        ListNode* ret = Solution().reverseList(head);
        
        string out = listNodeToString(ret);
        cout << out << endl;
    }
    return 0;
}
