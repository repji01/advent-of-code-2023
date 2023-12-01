import re
import sys
import copy
import heapq
import string

from importlib.util  import find_spec
from functools import lru_cache, reduce, partial
from collections import defaultdict, deque, namedtuple, Counter
from operator import itemgetter, attrgetter, methodcaller

if find_spec('z3') is not None:
	import z3

if find_spec('blist') is not None:
	import blist

if find_spec('sortedcontainers') is not None:
	import sortedcontainers

if find_spec('numpy') is not None:
	try:
		import numpy as np
	except ImportError:
		pass

if find_spec('networkx') is not None:
	import networkx as nx