import check50

import pandas as pd
import numpy as np
import os
import re

def spawn_small():
    return check50.spawn("python3 adventure.py Tiny")

def spawn_large():
    return check50.spawn("python3 adventure.py Small")

def spawn_crowther():
    return check50.spawn("python3 adventure.py Crowther")

@check50.check()
def exists(self):
    """Checking if all files exist."""
    self.require("degrees.py", "util.py")

    cwd = os.getcwd()
    dest = os.path.join(cwd, "data")
    if os.path.exists(dest):
        os.rename(dest, dest + str(uuid.uuid4()))
    os.mkdir(dest)
    with check50.cd(check50.config.check_dir):
        data_files = [os.path.join("data", data_file) for data_file in os.listdir("data")]
        for path in data_files:
            check50.copy(path, dest)
