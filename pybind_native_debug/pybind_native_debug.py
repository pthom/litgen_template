#!/usr/bin/env python3
from __future__ import annotations

import os
import sys

import daft_lib

THIS_DIR = os.path.dirname(__file__)


def main() -> None:
    sum = daft_lib.add(1, 2)
    print(sum)


main()
