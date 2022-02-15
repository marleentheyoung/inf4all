import check50

import pandas as pd
import numpy as np
import os
import re

class Degrees():
    def spawn_small(self):
        return self.check50.spawn("python3 degrees.py small")

    def spawn_large():
        return self.check50.spawn("python3 degrees.py large")

    @check50.check()
    def exists(self):
        """Checking if all files exist."""
        self.exists("degrees.py")

    @check50.check()
    def check_path(self):
        check = self.spawn_small()
        check.stdin("Emma ")
        raise NotImplementedError

