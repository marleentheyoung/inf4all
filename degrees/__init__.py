from sys import stdin
from check50 import *
from check50 import Checks 

import pandas as pd
import numpy as np
import os
import re
import uuid

# @check50.check()
# def exists():
#     """Checking if all files exist."""
#     exists("degrees.py")
class Degrees(Checks):


    @check()
    def check_path(self):
        """ Correctly finds path in small dataset """
        check = self.spawn("python3 degrees.py small").stdin("Emma Watson").stdin("Kevin Bacon")
        # check.stdout(re.escape("Not connected"), str_output="Not connected")
        
        # Check if path has been found
        # check.stdout(re.escape("Not connected."))

        # code = check50.run("./hello").exit()
        # if code != 0:
        #     raise check50.Failure(f"expected exit code 0, not {code}")
