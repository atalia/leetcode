/*
687. Longest Univalue Path
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:

2
Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output:

2
Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.


*/
#include <iostream>
#include <cctype>
#include <string>
#include <cstdlib>
#include <queue>
#include <sstream>
#include <algorithm>
using namespace std;
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
  };
class Solution {
public:
    int longestUnivaluePath(TreeNode* root) {
        if (root==NULL)
            return 0;
        int tmp = max(longestUnivaluePath(root->left), longestUnivaluePath(root->right));
        tmp = max(tmp, isSame(root->left,root->val)+isSame(root->right, root->val));
        return tmp;
    }
private:
    //获得单边最大长度
    int isSame(TreeNode* root,int val)
    {
        if(root==NULL || root->val!=val)
            return 0;
        return max(isSame(root->left,val),isSame(root->right, val))+1;
    }
};

void trimLeftTrailingSpaces(string &input) {
    input.erase(input.begin(), find_if(input.begin(), input.end(), [](int ch) {
        return !isspace(ch);
    }));
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

int main() {
    string line;
    while (getline(cin, line)) {
        TreeNode* root = stringToTreeNode(line);
        
        int ret = Solution().longestUnivaluePath(root);
        
        string out = to_string(ret);
        cout << out << endl;
    }
    return 0;
}
