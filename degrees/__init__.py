import check50

import pandas as pd
import numpy as np
import os
import re


def spawn_small():
    return check50.spawn("python3 degrees.py small")

def spawn_large():
    return check50.spawn("python3 degrees.py large")

# @check50.check()
# def exists():
#     """Checking if all files exist."""
#     exists("degrees.py")

@check50.check()
def check_path():
    check = spawn_small()
    check.stdin("Emma Watson")
    check.stdin("Kevin Bacon").stdout("Not connected.")
