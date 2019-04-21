
/*
200. Number of Islands
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
*/
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        if(grid.size() == 0)
            return 0;
        isvisited = vector<vector<int>> (grid.size(),vector<int>(grid[0].size(),0));
        for(int i = 0;i<grid.size();++i)
            for(int j = 0;j<grid[i].size();++j)
                if(grid[i][j] == '1'&& isvisited[i][j]==0)
                {
                    ++island;
                    dfs(i,j,grid);
                }
        return island;
    }
private:
    int island = 0;
    vector<vector<int>> isvisited;
    void dfs(int i,int j,const vector<vector<char>>& grid)
    {
        if(isvisited[i][j] == 1)
            return;
        isvisited[i][j] = 1;
        if(i-1>=0 && grid[i-1][j]=='1')
            dfs(i-1, j, grid);
        if(i+1<grid.size() && grid[i+1][j]=='1')
            dfs(i+1,j,grid);
        if(j-1>=0 && grid[i][j-1]=='1')
            dfs(i, j-1,grid);
        if(j+1<grid[0].size() && grid[i][j+1]=='1')
            dfs(i, j+1,grid);
    }
};