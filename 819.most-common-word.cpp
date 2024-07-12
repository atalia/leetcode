/*
 * @lc app=leetcode id=819 lang=cpp
 *
 * [819] Most Common Word
 */

// @lc code=start
#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<algorithm>
using namespace std;
class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        map<string, int> dict;
        int start = 0;
        for(int i = 0; i < paragraph.size(); i++){
            if(isalpha(paragraph[i])){
                paragraph[i] = tolower(paragraph[i]);
            }
            else{
                if(i - start > 0) {
                    string word = paragraph.substr(start, i - start);
                    if(banned.end() == find(banned.begin(), banned.end(), word)){
                        if(dict.find(word) == dict.end()){
                            dict[word] = 0;
                        }
                        dict[word]++;
                    }
                }
                start = i + 1;
            }
        }
        
        if(isalpha(paragraph[paragraph.size() - 1])){
            string word = paragraph.substr(start, paragraph.size() - start);
            if(banned.end() == find(banned.begin(), banned.end(), word)){
                if(dict.find(word) == dict.end()){
                    dict[word] = 0;
                }
                dict[word]++;
            }
        }
        
        string ret = dict.empty()?"":dict.begin()->first;
        for(auto it = dict.begin(); it != dict.end(); it++){
            if(it->second > dict[ret]){
                ret = it->first;
            }
        }
        return ret;
    }
};

int main(){
    string paragraph = "Bob";
    vector<string> banned = {"hit"};
    Solution s;
    cout << s.mostCommonWord(paragraph, banned);
    return 0;
}// @lc code=end

