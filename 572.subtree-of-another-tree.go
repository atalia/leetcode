/*
 * @lc app=leetcode id=572 lang=golang
 *
 * [572] Subtree of Another Tree
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

 func isSubtree(s *TreeNode, t *TreeNode) bool {
    if helper(s, t){
		return true
	}
	if s != nil && isSubtree(s.Left, t){
		return true
	}
	if s != nil &&isSubtree(s.Right, t){
		return true
	}
	return false
}

func helper(this *TreeNode, that *TreeNode) bool {
	if this == nil  && that == nil{
		return true
	}else if this == nil || that == nil{
		return false
	} 

	if this.Val != that.Val{
		return false
	}
	return helper(this.Left, that.Left) && helper(this.Right, that.Right)
}
// @lc code=end

