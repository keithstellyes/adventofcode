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
(Except for day 1)
I also initially write shared.py before I see part 2, trying to guess how
it might be extended. Of course, inevitably it will likely have to change.
Starting with Day 3, I use Git commit history to track changes made to accomodate part 2.

Some things missing/possible "improvements"
- Error Handling
  - I decide not to do this for simplicity's sake, and for readability of
    logic and solution

# Progress
2022:
- [x] Day 1
- [x] Day 2
- [x] Day 3
- [x] Day 4
- [x] Day 5

2021:
- [x] Days 1-2

# Callouts

2022-04 - overloading Python `in` operator, `shared.py` did not require rewrite
for pt 2

2022-2 - bit of a refactor to accomodate Pt 2
