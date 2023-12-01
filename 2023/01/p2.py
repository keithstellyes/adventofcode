import sys
total = 0
digits = {"one": 1, "two":2, "three":3, "four":4, "five":5, "six":6,
          "seven": 7, "eight": 8, "nine": 9}
for line in open(sys.argv[1], 'r'):
    i = 0
    curr_num = 0
    while i < len(line):
        dfound = False
        for ds, dd in digits.items():
            if line[i:].startswith(ds):
                i += 1
                dfound = True
                if curr_num == 0:
                    curr_num = dd * 10
                else:
                    curr_num = 10 * (curr_num // 10)
                    curr_num += dd
                break
        if not dfound and line[i].isdigit():
            d = int(line[i])
            i += 1
            if curr_num == 0:
                curr_num = d * 10
            else:
                curr_num = 10 * (curr_num // 10)
                curr_num += d
        elif not dfound and not line[i].isdigit():
            i += 1
    # single digit case
    # if there's only one digit, then it is the first AND the last
    if curr_num % 10 == 0:
        curr_num += curr_num // 10
    assert curr_num <= 99
    total += curr_num
print(total)
