/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <vector>
#include <queue>
#include <sstream>
#include <cctype>
using namespace std;
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
class Solution {
public:
    bool findTarget(TreeNode* root, int k) {
        map<int,int> nums;
        if(root==NULL)
            return false;
        queue<TreeNode*> tree;
        TreeNode * tmp = NULL;
        tree.push(root);
        while(tree.size()>0)
        {
            tmp = tree.front();
            if(nums[k-tmp->val]==1)
                return true;
            if(tmp->left!=NULL)
                tree.push(tmp->left);
            if(tmp->right!=NULL)
                tree.push(tmp->right);
            nums[tmp->val] = 1;
            tree.pop();
        }
        return false;
    }
};

void trimLeftTrailingSpaces(string &input) {
    input.erase(input.begin(), find_if(input.begin(), input.end(), [](int ch){return !isspace(ch);}));
}

TreeNode* stringToTreeNode(string input) {
    input = input.substr(1, input.length() - 2);
    if (!input.size()) {
        return nullptr;
    }
    
    string item;
    stringstream ss;
    ss.str(input);
    
    getline(ss, item, ',');
    TreeNode* root = new TreeNode(stoi(item));
    queue<TreeNode*> nodeQueue;
    nodeQueue.push(root);
    
    while (true) {
        TreeNode* node = nodeQueue.front();
        nodeQueue.pop();
        
        if (!getline(ss, item, ',')) {
            break;
        }
        
        trimLeftTrailingSpaces(item);
        if (item != "null") {
            int leftNumber = stoi(item);
            node->left = new TreeNode(leftNumber);
            nodeQueue.push(node->left);
        }
        
        if (!getline(ss, item, ',')) {
            break;
        }
        
        trimLeftTrailingSpaces(item);
        if (item != "null") {
            int rightNumber = stoi(item);
            node->right = new TreeNode(rightNumber);
            nodeQueue.push(node->right);
        }
    }
    return root;
}

int stringToInteger(string input) {
    return stoi(input);
}

string boolToString(bool input) {
    return input ? "True" : "False";
}

int main() {
    string line;
    while (getline(cin, line)) {
        TreeNode* root = stringToTreeNode(line);
        getline(cin, line);
        int k = stringToInteger(line);
        
        bool ret = Solution().findTarget(root, k);
        
        string out = boolToString(ret);
        cout << out << endl;
    }
    return 0;
}