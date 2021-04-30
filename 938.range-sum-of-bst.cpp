/*
 * @lc app=leetcode id=938 lang=cpp
 *
 * [938] Range Sum of BST
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 */
// #include<iostream>
// using namespace std;
// struct TreeNode {
//     int val;
//     TreeNode *left;
//     TreeNode *right;
//     TreeNode() : val(0), left(nullptr), right(nullptr) {}
//     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
//     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
// };

class Solution {
public:
    int rangeSumBST(TreeNode* root, int low, int high) {
        if(root == nullptr){
            return 0;
        }
        int left = 0, right = 0, value = 0;
        if(root->val >= low && root->val <= high){
            value = root->val;
        }
        if(root->val > low){
            left = rangeSumBST(root->left, low, high);
        }
        if(root->val < high){
            right = rangeSumBST(root->right, low, high);
        }
        return value + right + left;
    }
};

// int main(){
//     TreeNode *root = new TreeNode(10);
//     root->left = new TreeNode(5);
//     root->left->left = new TreeNode(3);
//     //root->left->left->left = new TreeNode(1);
//     root->left->right = new TreeNode(7);
//     //root->left->right->left = new TreeNode(6);

//     root->right = new TreeNode(15);
//     //root->right->left = new TreeNode(13);
//     root->right->right = new TreeNode(18);

//     std::cout << Solution().rangeSumBST(root, 7, 15);
// }
// @lc code=end

