/*
 * @lc app=leetcode id=844 lang=cpp
 *
 * [844] Backspace String Compare
 */

// @lc code=start

// #include<string>
// #include<stack>
// #include<iostream>
// using namespace std;

class Solution {
public:
    bool backspaceCompare(string s, string t) {
        return getString(s) == getString(t);
    }

private:
    string getString(string s){
        stack<char> st;
        for(int i=0;i<s.size();i++){
            if(s[i]=='#'){
                if(!st.empty())
                    st.pop();
            }
            else{
                st.push(s[i]);
            }
        }
        string ans="";
        while(!st.empty()){
            ans+=st.top();
            st.pop();
        }
        return ans;
    }
};

// int main() {
//     cout << (Solution().backspaceCompare("a#c", "b") ? "true" : "false") << endl;;
// }

// @lc code=end

