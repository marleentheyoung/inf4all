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

@check50.check("exists")
def handles_argument(self):
    """Starting adventure with command line argument 'Tiny'."""
    try:
        self.spawn_tiny().stdout(re.escape(room_1_description), str_output=room_1_description)
    except Error as error:
        raise Error(rationale=f"Expected the description of initial "
                                f"room when Adventure starts.\n    {error}")

@check50.check("handles_argument")
def rejects_incorrect_arguments(self):
    """Rejects incorrect amount of arguments or wrong filename."""
    try:
        self.spawn("python3 adventure.py").exit(1)
    except Error as error:
        raise Error(rationale=f"Expected an exit code of 1. Not {error}")

    try:
        self.spawn("python3 adventure.py Tiny CS50").exit(1)
    except Error as error:
        raise Error(rationale=f"Expected an exit code of 1. Not {error}")

    try:
        self.spawn("python3 adventure.py CS50").exit(1)
    except Error as error:
        raise Error(rationale=f"Expected an exit code of 1. Not {error}")
