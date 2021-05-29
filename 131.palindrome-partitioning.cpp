/*
 * @lc app=leetcode id=131 lang=cpp
 *
 * [131] Palindrome Partitioning
 */

// @lc code=start
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution
{
private:
    vector<vector<int> > record;
    vector<vector<string> > result;
    vector<string> cur;
    int ispalindrome(const string &s, int i, int j)
    {
        if (i >= j)
        {
            return true;
        }
        if (record[i][j] == -1)
        {
            if (s[i] == s[j]){
                record[i][j] = ispalindrome(s, i + 1, j - 1);
            }else{
                record[i][j] = 0;
            }
            
        }
        return record[i][j];
    }

    void dfs(string s, int i)
    {
        if (i == s.size())
        {
            result.push_back(cur);
            return;
        }
        for (int j = i; j < s.size(); ++j)
        {
            if (ispalindrome(s, i, j) == 0)
            {
                continue;
            }
            else
            {
                cur.push_back(s.substr(i, j-i+1));
                dfs(s, j + 1);
                cur.pop_back();
            }
        }
    }
public:
    vector<vector<string> > partition(string s)
    {
        record = vector<vector<int> >(s.size(), vector<int>(s.size(), -1));
        result = vector<vector<string> >();
        for (int i = 0; i < record.size(); ++i)
        {
            record[i][i] = 1;
        }
        dfs(s, 0);
        return result;
    }

    
};

int main()
{
    vector<vector<string> > r = Solution().partition("aab");
    for(auto &e : r){
        for (auto &ee : e){
            cout << ee << ", ";
        }
        cout << endl;
    }
    return 0;
}
// @lc code=end
