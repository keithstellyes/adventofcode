# based on geeksforgeeks maxheap
# however, their implementation ahs a bug where it assumes every node
# has 2 children, or 0 children. this fixes that

class Heap:
    def __init__(self):
        self.values = []
        self.__size = 0
    def _size(self):
        return self.__size
    def _parent(self, idx):
        return (idx - 1) // 2 
    def _lchild(self, idx):
        return (2 * idx) + 1
    def _rchild(self, idx):
        return (2 * idx) + 2
    def _isleaf(self, idx):
        return (idx > (self._size() // 2)) and idx <= self._size()

    def _swap(self, idx1, idx2):
        tmp = self.values[idx1]
        self.values[idx1] = self.values[idx2]
        self.values[idx2] = tmp

    def _maxheapify(self, idx):
        if self._isleaf(idx):
            return
        cur = self.values[idx]
        li = self._lchild(idx)
        ri = self._rchild(idx)
        if self._valididx(li):
            lchild = self.values[li]
        else:
            lchild = float('-inf')
        if self._valididx(ri):
            rchild = self.values[ri]
        else:
            rchild = float('-inf')
        if lchild > rchild:
            self._swap(idx, li)
            self._maxheapify(li)
        if rchild > lchild:
            self._swap(idx, ri)
            self._maxheapify(ri)
    def _valididx(self, idx):
        return idx >= 0 and idx < len(self.values)
    def insert(self, val):
        self.values.append(val)
        cur = self._size()
        while self.values[cur] > self.values[self._parent(cur)]:
            self._swap(cur, self._parent(cur))
            cur = self._parent(cur)
            if not self._valididx(cur) or not self._valididx(self._parent(cur)):
                break
        self.__size += 1
    def pop(self):
        val = self.values[0]
        self.values[0] = self.values[-1]
        del self.values[-1]
        self.__size -= 1
        self._maxheapify(0)
        return val

