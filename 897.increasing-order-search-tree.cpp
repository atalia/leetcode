/*
 * @lc app=leetcode id=897 lang=cpp
 *
 * [897] Increasing Order Search Tree
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* increasingBST(TreeNode* root) {
        if(root == nullptr) {
            return root;
        }

        TreeNode* left = nullptr;
        if(root->left) {
            left = increasingBST(root->left);
        }

        TreeNode* right = nullptr;
        if(root->right){
            right = increasingBST(root->right);
        }

        if(left){
            TreeNode* preNode = left;
            while(preNode && preNode -> right){
                preNode  = preNode -> right;
            }
            preNode -> right = new TreeNode(root->val, nullptr, right);
            return left;
        } else {
            return new TreeNode(root->val, nullptr, right);
        }
    }
};
// @lc code=end

