class MaxHeap:
    def __init__(self):
        self.h = []

    def insert(self, val):
        self.h.append(val)
        self._heapify_up(len(self.h) - 1)

    def delete(self):
        if len(self.h) == 0:
            return None
        if len(self.h) == 1:
            return self.h.pop()
        max_val = self.h[0]
        self.h[0] = self.h.pop()
        self._heapify_down(0)
        return max_val

    def get_max(self):
        if not self.h:
            return None
        return self.h[0]

    def _heapify_up(self, idx):
        p_idx = (idx - 1) // 2
        if p_idx >= 0 and self.h[idx] > self.h[p_idx]:
            self.h[idx], self.h[p_idx] = self.h[p_idx], self.h[idx]
            self._heapify_up(p_idx)

    def _heapify_down(self, idx):
        largest = idx
        l_idx = 2 * idx + 1
        r_idx = 2 * idx + 2

        if l_idx < len(self.h) and self.h[l_idx] > self.h[largest]:
            largest = l_idx

        if r_idx < len(self.h) and self.h[r_idx] > self.h[largest]:
            largest = r_idx

        if largest != idx:
            self.h[idx], self.h[largest] = self.h[largest], self.h[idx]
            self._heapify_down(largest)
            
heap = MaxHeap()
heap.insert(10)
heap.insert(20)
heap.insert(5)
print(heap.get_max())
print(heap.delete())
print(heap.get_max())