/*
257. Binary Tree Paths
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
*/
#include <iostream>
#include <cctype>
#include <string>
#include <cstdlib>
#include <queue>
#include <sstream>
using namespace std;
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
  };
class Solution {
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<int> num;
        dfs(root,num);
        vector<string> result;
        string tmp;
        int i,j;
        for(i = 0;i<nums.size();++i)
        {
            tmp.clear();
            for(j = 0;j<nums[i].size()-1;++j)
            {
                tmp += output(nums[i][j])+string("->");
            }
            tmp += output(nums[i][j]);
            result.push_back(tmp);
        }
        return result;
    }
private:
    vector<vector<int>> nums;
    void dfs(TreeNode* root,vector<int> num)
    {
        if(root == NULL)
            return;
        num.push_back(root->val);
        if(root->left == NULL && root->right == NULL)
        {
            nums.push_back(num);
            return;
        }
        dfs(root->right,num);
        dfs(root->left,num);
    }
    string output(int n)
    {
        stringstream ss;
        ss<<n;
        return ss.str();
    }
};
int main()
{
    TreeNode *root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->right = new TreeNode(4);
    root->left->left = new TreeNode(5);
    vector<string> result = Solution().binaryTreePaths(root);
    for (int i = 0; i<result.size(); ++i) {
        cout<<result[i]<<endl;
    }
    return 0;
}
