#!/usr/bin/env python3

# Author: Abhyjit Singh Kohri
# Author ID: 142112226
# Date Created: 2024/05/22

import sys

if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    timer = 3

while timer > 0:
    print(timer)
    timer -= 1

# Blast off!
print("blast off!")
