#!/bin/env bash
INPUT="input"

# 1. Delete trailing newline to normalize
# 2. Use _ instead of \n to separate bags to simplify parsing
# 3. separate items in bags with a + instead of \n so it can become input for bc
# 4. Use bc (standard linux calc program) to compute each line
# 5. now that each line is the sum of each bag, we can sort it ascending order
# 6. Last result is max
cat $INPUT | sed -z '$s/\n$//' \
    | sed -z 's/\n\n/_/g' \
    | sed -z 's/\n/+/g' \
    | sed 's/_/\n/g' \
    | sed '$s/$/\nquit/' \
    | bc \
    | sort -n \
