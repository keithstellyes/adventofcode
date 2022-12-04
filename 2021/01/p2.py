import sys, shared

WINDOW_SIZE = 3

class Windows:
    def __init__(self):
        self.values = []
        self.total = 0
    def on_depth(self, depth):
        self.values.append(depth)
        if len(self.values) <= WINDOW_SIZE:
            return
        if self.get_new_window() > self.get_old_window():
            self.total += 1
        assert len(self.values) == WINDOW_SIZE + 1
        del self.values[0]
    def _get_window_off(self, off):
        total = 0
        for i in range(1, WINDOW_SIZE + 1):
            total += self.values[-i - off]
        return total
    def get_old_window(self):
        return self._get_window_off(1)
    def get_new_window(self):
        return self._get_window_off(0)
w = Windows()
shared.parse(sys.argv[1], w.on_depth)
print(w.total)
