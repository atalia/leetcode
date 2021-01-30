/*
 * @lc app=leetcode id=959 lang=cpp
 *
 * [959] Regions Cut By Slashes
 */

// @lc code=start
#include<iostream>
#include<vector>
#include<string>
using namespace std;

class Solution {
private:
    vector<int> root_p;
    int cnt;
public:
    int regionsBySlashes(vector<string>& grid) {
        int n = grid.size();
        root_p = vector<int>(4 * n * n, 0);
        cnt = 4 * n * n;
        for(int i = 0; i< root_p.size(); ++i){
            root_p[i] = i;
        }
        //print_root();
        
        int p0, p1, p2, p3;
        for(int row=0; row < n; ++row){
            for(int col=0; col < n; ++col) {
                p0 = 4 * (row * n + col) ;
                p1 = p0 + 1;
                p2 = p1 + 1;
                p3 = p2 + 1;
                if (col < n - 1){
                    union_m(p2, p0 + 4);
                }
                if( row < n - 1){
                    union_m(p3, p0 + 4 * n + 1);
                }
                
                if(grid[row][col] == '/'){
                    union_m(p0, p1);
                    union_m(p2, p3);

                }else if (grid[row][col] == '\\')
                {
                    union_m(p0, p3);
                    union_m(p1, p2);
                }else{
                    union_m(p0, p1);
                    union_m(p0, p2);
                    union_m(p0, p3);
                }
                
            }
            //print_root();
        }
        //print_root();
        return cnt;
    }

    int find_m(int x){
        if(root_p[x] == x) {
            return x;
        }
        int parent = x;
        while(parent != root_p[parent]){
            parent = root_p[parent];
        }
        int m;
        while(x != parent){
            m = root_p[x];
            root_p[x] = parent;
            x = m;
        }

        return parent;
    }

    void union_m(int x, int y) {
        int x_r = find_m(x);
        int y_r = find_m(y);
        if(x_r != y_r){
            root_p[y_r] = x_r;
            cnt -= 1;
        }
    }

    void print_root(){
        for(auto &elem : root_p) {
            cout << elem << " ";
        }
        cout << std::endl;
    }
};


// int main(){
//     vector<string> input = {"//", "/ "};
//     cout << Solution().regionsBySlashes(input) << endl;
//     return 0;
// }
// @lc code=end

