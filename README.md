# leetcode  

## Thanks

[![logo](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/PyCharm_Logo.svg/220px-PyCharm_Logo.svg.png)](https://www.jetbrains.com/?from=leetcode)

## 好好学习，天天向上  
* ### 687 关于递归的好题目  
* ### 206 链表反转的两种实现方式  
* ### 279 这个题目的关键是无法确定之前子集求出的结果为最优，所以用递归求解的时候存在大量无法避免的重复计算，改为循环更新  
* ### 91, 139 递归效率极低，今后动态规划有限考虑数组更新  

* ### 120 240 神题

* ### 213 问题转换 not(A and B) == not A or not B

* ### 142 解题思路  
    1. 首先利用移动速度2的指针和移动速度1的指针，判断是否有环  
    2. 如果两个指针指向同一个Node， 该Node一定在环内，假设 该Node距离环入口**x**个Node,环前有**a**个Node，环内有**c**个Node，移动了**s**个步骤：  
        移动速度1的指针移动了 ```x + a```个Node,则  ```x + a = s ```
        移动速度2的指针移动了```x + a + nc```,其中n为正整数```x + a + nc= 2 * s ```
    3. 因此, ```(x + a) mod c == 0``` ==> ```(c - x - a) mod c == 0```，假设把其中一个指针放到head位置，另一个保持原位置，两者移动速度为1, 移动2个指针直至相遇, 此时```(c - x- a) mod c == 0```==> ```a +  Mc= c - x + Nc, M、N 为正整数```,即证明了两个指针一定会在环入口处相遇！

* ### 79 非常有意思的一题  
    思路上没任何问题，DFS  
    但有一个细节需要注意，就是是用一个全局变量标识是否存在该字符串，还是直接return结果区别如下  
    1. 如果使用全局变量，则会遍历在某些特殊情况下遍历所有可能的答案，这会浪费大量的时间去回溯。  
    2. 如果找到一个满足答案的解法，直接return  
    方法1 适合求**所有的解法**， 方法2 适合判断**是否存在解法**

* ### 11 挺有意思的一个题目

* ### 48 Marked

* ### 78 bit-manipulation 解法有点意思

* ### 94 https://en.wikipedia.org/wiki/Threaded_binary_tree
整理下thread_binary_tree构造流程

thread_binary_tree 可以实现空间复杂度1 对二叉树中序遍历

1. 如果root为空,退出
2. 如果root不存在左节点，输出节点，同时root=root.right,回到1
3. 如果root存在左节点，那么找出root.left的最右子节点
- 存在最右子节点（不存在环），将root.left的最右子节点（可以是root.left 的右子节点）指向root,然后root = root.left, 回到1
- 不存在最右子节点（存在环，寻找最右子节点经过了root），输出root节点，将指向root节点右节点置空，同时root = root.right，回到1

 ```python
 def inorderTraversal(TreeNode root)
    # 1
    if not root:
        return []
    cur = root
    nodes = []
    while cur:
        # 2
        if not cur.left:
            nodes.append(cur.val)
            cur = cur.right
        pre = cur.left:
        while pre.right and pre.right is not cur:
            pre = pre.right
        #  3
        if not pre.right:
            pre.right = cur
            cur = cur.left
        else:
            pre.right = None
            nodes.append(cur.val)
            cur = cur.right
 ```

* ###236待优化

* ###146待整理

* ###212

* ###456

* ###45 

* ### 148 链表归并排序
这道题需要注意个细节，当fast指针到达尾部时，slow需要做切割，`slow.next=None`将链表分为2个部分，否则后续递归时，left链表还是原链表，死循环。