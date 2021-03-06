/*
437. Path Sum III
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
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
    int pathSum(TreeNode* root, int sum) {
       if(root == NULL)
           return 0;
        dfs(root,sum);
        pathSum(root->left,sum);
        pathSum(root->right, sum);
        return cnt;
    }
private:
    int cnt = 0;
    void dfs(TreeNode* root,int sum)
    {
        if(root == NULL)
            return ;
        if(sum == root->val)
            ++cnt;
        dfs(root->left, sum-root->val);
        dfs(root->right, sum-root->val);
    }
};
int main()
{
    TreeNode *root = new TreeNode(10);
    root->left = new TreeNode(5);
    root->left->left = new TreeNode(3);
    root->left->left->left = new TreeNode(3);
    root->left->left->right = new TreeNode(-2);
    root->left->right = new TreeNode(2);
    root->left->right->right = new TreeNode(1);
    root->right = new TreeNode(-3);
    root->right->left = new TreeNode(11);
    cout<<Solution().pathSum(root, 8)<<endl;
    return 0;
}
