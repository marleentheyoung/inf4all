from sys import stdin
import check50

import pandas as pd
import numpy as np
import os
import re
import uuid

# @check50.check()
# def exists():
#     """Checking if all files exist."""
#     exists("degrees.py")

@check50.check()
def check_path():
    """ Correctly finds path in small dataset """
    check = check50.run("python3 degrees.py small").stdin("Emma Watson", prompt=True).stdin("Kevin Bacon", prompt=True)
    
    # Check if path has been found
    check.stdout(re.escape("Not connected."))

    # code = check50.run("./hello").exit()
    # if code != 0:
    #     raise check50.Failure(f"expected exit code 0, not {code}")
