/*
 * @lc app=leetcode id=97 lang=cpp
 *
 * [97] Interleaving String
 */

// @lc code=start
#include <iostream>
#include <string>
#include <vector>
using namespace std;

void print(vector<vector<int>> &m);

class Solution
{
public:
    bool isInterleave(string s1, string s2, string s3)
    {
        if (s1.size() + s2.size() != s3.size())
        {
            return false;
        }
        vector<vector<int>> dp(s1.size() + 1, vector<int>(s2.size() + 1, 0));
        dp[0][0] = 1;
        for (int i = 0; i < dp.size(); ++i)
        {
            for (int j = 0; j < dp[0].size(); ++j)
            {
                if (i > 0)
                {
                    dp[i][j] |= (dp[i - 1][j] & (s1[i - 1] == s3[i + j - 1]));
                }
                if (j > 0)
                {
                    dp[i][j] |= (dp[i][j - 1] & (s2[j - 1] == s3[i + j - 1]));
                }
                //dp[i][j] = (dp[i-1][j] & (s1[i-1] == s3[i+j-1])) | (dp[i][j-1] & (s2[j-1] == s3[i+j-1]));
            }
        }
        //print(dp);
        return dp[s1.size()][s2.size()] == 1;
    }
};

void print(vector<vector<int>> &m)
{
    for (int i = 0; i < m.size(); ++i)
    {
        for (int j = 0; j < m[0].size(); ++j)
        {
            cout << m[i][j] << " ";
        }
        cout << endl;
    }
}

int main(int argc, char *argv[])
{
    // if (argc < 4){
    //     return 1;
    // }
    // cout << Solution().isInterleave(argv[1], argv[2], argv[3]) << endl;
    cout << Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac") << endl;
    cout << Solution().isInterleave("aabcc",  "dbbca" ,"aadbbbaccc") << endl;
    //cout << Solution().isInterleave("", "", "") << endl;
    return 0;
}
// @lc code=end
