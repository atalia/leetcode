/*
 * @lc app=leetcode id=993 lang=cpp
 *
 * [993] Cousins in Binary Tree
 */

// @lc code=start

// * Definition for a binary tree node.

#include<iostream>
#include<queue>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
 
class Solution {
public:

    bool isCousins(TreeNode* root, int x, int y) {
        if(!root || root->val == x || root->val == y){
            return false;
        }
        queue<TreeNode*> next;
        queue<TreeNode*> cur;
        cur.push(root);
        TreeNode* node = nullptr;
        TreeNode* x_parent = nullptr;
        TreeNode* y_parent = nullptr;
        int depth = 0;
        int depth_x = 0, depth_y = 0;
        while(cur.size()){
            while(cur.size()){
                node = cur.front();
                cur.pop();
                if(node->left){
                    next.push(node->left);
                    if(node->left-> val == x){
                        x_parent = node;
                        depth_x = depth;
                    }
                    if(node->left->val ==y){
                        y_parent = node;
                        depth_y = depth;
                    }
                }
                if(node->right){
                    next.push(node->right);
                    if(node->right-> val == x){
                        x_parent = node;
                        depth_x = depth;
                    }
                    if(node->right->val ==y){
                        y_parent = node;
                        depth_y = depth;
                    }
                }
            }
            depth += 1;
            cur = next;
            next = queue<TreeNode*>();
            if (depth_x != 0 && depth_y != 0){
                break;
            }
        }
        return (x_parent != y_parent && depth_x == depth_y);
    }
    
};

// int main(){
//     TreeNode* root = new TreeNode(1);
//     root->left = new TreeNode(2);
//     root->right = new TreeNode(3);
//     root->left->right = new TreeNode(4);
//     //root->right->right = new TreeNode(5);

//     cout << Solution().isCousins(root, 2, 3);
// }
// @lc code=end

