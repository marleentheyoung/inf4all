"""
Created on Tues Feb 15

@author: Marleen de Jonge
"""

import re
import os
import uuid

from check50 import *
import check50

class Adventure():
    def spawn_small(self):
        return self.spawn("python3 degrees.py Tiny")

    def spawn_large(self):
        return self.spawn("python3 degrees.py large")