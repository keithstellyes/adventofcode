import sys
import maxheap

f = open(sys.argv[1], 'r')
curr_elf = 0
heap = maxheap.Heap()
for l in f:
    l = l.strip()
    if l == '':
        heap.insert(curr_elf)
        curr_elf = 0
    else:
        calories = int(l)
        curr_elf += calories
heap.insert(curr_elf)
print(sum([heap.pop() for i in range(3)]))
