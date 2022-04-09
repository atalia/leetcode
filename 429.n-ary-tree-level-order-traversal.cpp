/*
 * @lc app=leetcode id=429 lang=cpp
 *
 * [429] N-ary Tree Level Order Traversal
 */

// @lc code=start
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/
// #include<queue>
// #include<vector>
// #include<iostream>
// using namespace std;
// class Node {
// public:
//     int val;
//     vector<Node*> children;

//     Node() {}

//     Node(int _val) {
//         val = _val;
//     }

//     Node(int _val, vector<Node*> _children) {
//         val = _val;
//         children = _children;
//     }
// };

class Solution {
public:
    vector<vector<int>> levelOrder(Node* root) {
        vector<vector<int>> ret;
        if(!root){
            return ret;
        }
        queue<Node*> curNodes;
        curNodes.push(root);
        while(curNodes.size()){
            queue<Node*> nextNodes;
            vector<int> nodeValues;
            while(curNodes.size()){
                Node* node = curNodes.front();
                nodeValues.push_back(node->val);
                for(auto const &v: node->children) {
                    nextNodes.push(v);
                }
                curNodes.pop();
            }
            curNodes = nextNodes;
            ret.push_back(nodeValues);
        }
        return ret;
    }
};

// int main(){
//     Node* root = new Node(1);
//     vector<Node*> children;
//     children.push_back(new Node(1));
//     children.push_back(new Node(2));
//     children.push_back(new Node(3));
//     root->children = children;
//     vector<vector<int>> ret = Solution().levelOrder(root);
//     for (auto const& row: ret){
//         cout << "[";
//         for(auto const& col: row) {
//             cout << col <<", ";
//         }
//         cout << "]"<<endl;
//     }
// }
// @lc code=end

