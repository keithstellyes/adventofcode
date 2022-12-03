import sys

f = open(sys.argv[1], 'r')
elf_max = 0
curr_elf = 0
for l in f:
    l = l.strip()
    if l == '':
        if curr_elf > elf_max:
            elf_max = curr_elf
        curr_elf = 0
    else:
        calories = int(l)
        curr_elf += calories
if curr_elf > elf_max:
    elf_max = curr_elf
print(elf_max)
