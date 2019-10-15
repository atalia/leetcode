#
# @lc app=leetcode id=621 lang=python
#
# [621] Task Scheduler
#
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        cnt_dict = dict()
        for task in tasks:
            if task not in cnt_dict:
                cnt_dict[task] = 0
            cnt_dict[task] += 1
        tasks_key = cnt_dict.keys()
        tasks_key.sort(key=lambda x:cnt_dict[x], reverse=True)
        idx = 1
        while(idx < len(tasks_key) and cnt_dict[tasks_key[idx]] == cnt_dict[tasks_key[idx-1]]):
            idx += 1
        return max((n + 1) * (cnt_dict[tasks_key[0]] - 1) + idx, len(tasks))
        
            

