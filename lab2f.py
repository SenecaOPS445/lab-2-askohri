#!/usr/bin/env python3

# Author: Abhyjit Singh Kohri
# Author ID: 142112226
# Date Created: 2024/05/22

import sys

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <count>")
    sys.exit(1)

timer = int(sys.argv[1])

while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")
