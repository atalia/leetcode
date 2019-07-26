# coding:utf-8

class TreeNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self._head = None
        self._tail = None
        self._nodes = {}
        self._capacity = capacity
        self._size = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self._nodes:
            return -1
        node = self._nodes[key]
        if node is self._tail:
            return node.value
        else:
            if self._head is node:
                self._head = self._head.next
            else:
                node.pre.next = node.next
            node.next.pre = node.pre
            # to last
            self._tail.next = node
            node.pre = self._tail
            node.next = None
            self._tail = node
        return node.value


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self._nodes:
            node = ListNode(key, value)
            self._size += 1
            if self._size > self._capacity:
                self._nodes.pop(self._head.key)
                self._head = self._head.next
                if self._head:
                    self._head.pre = None
                else:
                    self._tail = None
                self._size -= 1
            if not self._head or not self._tail:
                self._head = node
            else:
                self._tail.next = node
            node.pre = self._tail
            self._tail = node
            self._nodes[key] = node
        else:
            node = self._nodes[key]
            if node is not self._tail:
                if node is self._head:
                    self._head = self._head.next
                else:
                    node.pre.next = node.next
                node.next.pre = node.pre
                self._tail.next = node
                node.pre = self._tail
                node.next = None
                self._tail = node



class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


def list_handle(put_or_get, data):
    cache = None
    for idx, manipulate in enumerate(put_or_get):
        if manipulate == 'put':
            cache.put(data[idx][0], data[idx][1])
        elif manipulate == 'get':
            cache.get(data[idx][0])
        else:
            cache = LRUCache(data[idx][0])


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(2,1)
    cache.put(2,2)
    print cache._nodes
    cache.get(2)
    print cache._nodes
    cache.put(1,1)
    print cache._nodes
    cache.put(4,1)
    print cache._nodes
    cache.get(2)
    print cache._nodes
    #from data import manipulate, data
    #print list_handle(manipulate, data)
    # cache = LRUCache(2)
    # cache.put(1,1)
    # cache.put(2,2)
    # cache.put(3,3)
    # cache.get(1)
    # cache.put(2,2)
    # cache.get(3)
    # cache.put(3,3)
    # cache.get(3)
