from sys import stdin
import check50

import pandas as pd
import numpy as np
import os
import re
import uuid


@check50.check()
def check_path(self):
    """ Correctly finds path in small dataset """
    try:
        check50.run("python3 degrees.py small").stdin("Emma Watson").stdin("Kevin Bacon").stdout("Not connected.", regex=False)
    
    