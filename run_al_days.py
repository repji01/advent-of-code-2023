#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""day01.py: Advent of Code 2023
   https://adventofcode.com/2023/
"""

__version__ = "1.0"
__maintainer__ = "Jiří Řepík"
__email__ = "jiri.repik@gmail.com"
__status__ = "Submited"

import os
import subprocess


if __name__ == "__main__":
    for day in range(1, 26):
        fname = "day0{}.py".format(day)
        if os.path.isfile(fname):
            subprocess.run(["python3", fname])