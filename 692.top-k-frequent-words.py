#
# @lc app=leetcode id=692 lang=python
#
# [692] Top K Frequent Words
#
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        w_d = dict()
        for word in words:
            if word not in w_d:
                w_d[word] = 0
            w_d[word] += 1
        heap = []
        for w_k in w_d.iterkeys():
            add_item(heap, w_k, w_d)
            if len(heap) > k:
                del_min_item(heap, w_d)
        res = []
        while heap:
            x = del_min_item(heap, w_d)
            res.append(x)
        res.reverse()
        print len(res)
        for idx, x in enumerate(res):
            print idx, x, w_d[x]
        return res

    
def del_min_item(heap, d):
    min_item = heap[0]
    parent = 0
    size = len(heap) - 1
    while 2 * parent + 1 < size:
        child = 2 * parent + 1
        if child + 1 < size and not smaller(heap[child], heap[child+1], d):
            child += 1
        if smaller(heap[-1] , heap[child], d):
            break
        else:
            heap[parent] = heap[child]
        parent = child
    heap[parent] = heap[-1]
    heap.pop()
    return min_item

def add_item(heap, item, d):
    heap.append(item)
    idx = len(heap) - 1
    while idx > 0 and not smaller(heap[(idx-1)/2], item, d):
        heap[idx] = heap[(idx-1)/2]
        idx = (idx-1)/2
    heap[idx] = item

def smaller(a, b, d):
    if d[a] < d[b]:
        return True
    elif d[a] > d[b]:
        return False
    else:
        return a > b
    




# if __name__ == '__main__':
#     #Input =  ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
#     #k = 4
#     Input = ["rmrypv","zgsedk","jlmetsplg","wnfbo","hnnftqf","bxlr","sviavwoxss","jdbgvc","zddeno","rxgw","hnnftqf","hdmvplne","rlmdt","jlmetsplg","ous","rmrypv","fwxulnpit","dmhuq","rxgw","ledleb","bxlr","indbvb","ckqqibnx","cub","ijww","ehd","hfhlfqzkcn","sviavwoxss","rxgw","bxjxpfp","mgqj","oic","ptk","fwxulnpit","ijww","sviavwoxss","bgfvfa","zfkgsudxq","alkq","dmhuq","zddeno","rxgw","zgsedk","amarxpg","bgfvfa","wnfbo","sviavwoxss","sviavwoxss","alkq","nmclxk","zgsedk","bwowfvira","ous","bxlr","zddeno","rxgw","ous","wnfbo","rmrypv","sviavwoxss","ehd","zgsedk","jlmetsplg","abxvhyehv","ledleb","wnfbo","bgfvfa","bwowfvira","amarxpg","wnfbo","bwowfvira","dmhuq","ouy","bxlr","rxgw","oic","hnnftqf","ledleb","rlmdt","oldainprua","ous","ckqqibnx","dmhuq","hnnftqf","oic","jlmetsplg","ppn","amarxpg","jlgfgwb","bxlr","bwowfvira","hdmvplne","oic","ledleb","bwowfvira","oic","ptk","dmhuq","abxvhyehv","ckqqibnx","indbvb","ypzfk","rmrypv","bxjxpfp","amarxpg","dmhuq","sviavwoxss","bwowfvira","zfkgsudxq","wnfbo","rxgw","jxkvrmajri","cub","abxvhyehv","bwowfvira","indbvb","ehd","ckqqibnx","oic","ptk","hnnftqf","ouy","oic","zgsedk","abxvhyehv","ypzfk","ptk","sviavwoxss","rmrypv","oic","ous","abxvhyehv","hnnftqf","hfhlfqzkcn","ledleb","cub","ppn","zddeno","indbvb","oic","jlmetsplg","ouy","bwowfvira","bklij","gucayxp","zfkgsudxq","hfhlfqzkcn","zddeno","ledleb","zfkgsudxq","hnnftqf","bgfvfa","jlmetsplg","indbvb","ehd","wnfbo","hnnftqf","rlmdt","bxlr","indbvb","jdbgvc","jlmetsplg","cub","jlgfgwb","ypzfk","indbvb","dmhuq","jlmetsplg","zgsedk","rmrypv","cub","rxgw","ledleb","rxgw","sviavwoxss","ckqqibnx","hdmvplne","dmhuq","wnfbo","jlmetsplg","bxlr","zfkgsudxq","bxjxpfp","ledleb","indbvb","ckqqibnx","ous","ckqqibnx","cub","ous","abxvhyehv","bxlr","hfhlfqzkcn","hfhlfqzkcn","oic","ten","amarxpg","indbvb","cub","alkq","alkq","sviavwoxss","indbvb","bwowfvira","ledleb"]
#     k = 41
#     #Input = ["i", "love", "leetcode", "i", "love", "coding"]
#     #k = 2
#     print Solution().topKFrequent(Input, k)
