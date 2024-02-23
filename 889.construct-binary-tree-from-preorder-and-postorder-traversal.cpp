/*
 * @lc app=leetcode id=889 lang=cpp
 *
 * [889] Construct Binary Tree from Preorder and Postorder Traversal
 */

// @lc code=start
#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
using namespace std;

 // Definition for a binary tree node.
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
    TreeNode* constructFromPrePost(vector<int>& preorder, vector<int>& postorder) {
        if(preorder.size() == 0)
            return nullptr;
        TreeNode* root = new TreeNode(preorder[0]);
        if(preorder.size() == 1)
            return root;
        
        int pos = 0;
        for(const auto& e: postorder){
            ++pos;
            if(e == preorder[1]){
                break;
            }
        }

        vector<int> left_a=vector<int>(preorder.begin()+1, preorder.begin()+pos+1);
        vector<int> left_b=vector<int>(postorder.begin(), postorder.begin()+pos);

        vector<int> right_a = vector<int>(preorder.begin()+pos+1, preorder.end());
        vector<int> right_b = vector<int>(postorder.begin()+pos, postorder.end()-1);

        root->left = constructFromPrePost(left_a, left_b);
        root->right = constructFromPrePost(right_a, right_b);
        return root;
    }
};

void print(TreeNode* root){
    if(!root){
        return;
    }
    queue<TreeNode*> q;
    q.push(root);
    while (!q.empty())
    {
        queue<TreeNode*> t;
        
        while(!q.empty()){
            auto node = q.front();
            cout<< node->val;
            if(node->left){
                t.push(node->left);
            }
            if(node->right){
                t.push(node->right);
            }
            q.pop();
        }
        q = t;
    }
    
}

int main(){
    vector<int> preorder={1,2,4,5,3,6,7};
    vector<int> postorder={4,5,2,6,7,3,1};

    auto t = Solution().constructFromPrePost(preorder,postorder );
    print(t);
    return 0;
}
// @lc code=end

