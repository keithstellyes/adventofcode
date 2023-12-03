# Explanation
This is for the [Advent of Code](https://adventofcode.com/2022). I try to generally write in a more-or-less extensible way, with this basic architecture:

```
p1.py ---+
 Part 1  |
         + - shared.py
         |       parse(filename, per_item_callback, misc)
         |       other shared logic
p2.py ---+
 Part 2
```
I also initially write shared.py before I see part 2, trying to guess how
it might be extended. Of course, inevitably it will likely have to change.
Starting with Day 3, I use Git commit history to track changes made to accomodate part 2.

Some things missing/possible "improvements"
- Error Handling
  - I decide not to do this for simplicity's sake, and for readability of
    logic and solution

# Languages used

Most code is Python, however starting for 2023 I plan on doing technologies other than Python. To experiment with how I want to do it, I've done a few other languages for 2022/01 (`awk`, `bash`, `common lisp`)

# Progress
2023:
- [x] Days 1-3

2022:
- [x] Days 1-14

2021:
- [x] Days 1-6

2020:
- [x] Day 1

2019:
- [x] Day 1-2, 5, 7, 9, 11, 13

# Callouts

2022-04 
- overloading Python `in` operator, `shared.py` did not require rewrite
for pt 2

2022-02:
- bit of a refactor to accomodate Pt 2

2022-06:
- Ring buffer!!!
- Didn't use a shared.py but didn't use magic numbers so was easier
to accomodate pt 2. To complete Pt 2, shared.py moved most p1 code to shared. Pt 1 and Pt 2 make the exact same function call except with a different integer parameter

2022-10:
- couple layers of callbacks

2022-11:
- Modular arithmetic required for sufficiently efficient solution

2019:
- A theme of this year was a custom CPU being built. Day 19 the puzzle was to
run a "Breakout" type game, and my solution hacks the game to make it play
itself/beatable (as it is difficult to actually beat, per the problem
specification...)

# Thanks

Thanks [Aaron Ellison](https://github.com/hath995) for helping with the Dafny code
