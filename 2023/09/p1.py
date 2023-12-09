#!/usr/bin/env python3
import sys
from shared import *

print(sum([extrapolate(h) for h in parsefn(sys.argv[1])]))
