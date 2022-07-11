import os
import sys

this_dir = os.path.dirname(__file__)
sys.path = [this_dir] + sys.path

from _example_lib import *
from _example_lib import __version__
