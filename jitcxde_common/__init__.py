from sys import version_info
if version_info < (3,3):
	raise NotImplementedError("Python versions below 3.3 are not supported anymore (or never were). Please upgrade to a newer Python version.")

from ._jitcxde import jitcxde, DEFAULT_COMPILE_ARGS, DEFAULT_LINK_ARGS, MSVC_COMPILE_ARGS, MSVC_LINK_ARGS
from .symbolic import conditional
from .check import checker

try:
	from .version import version as __version__
except ImportError:
	from warnings import warn
	warn('Failed to find (autogenerated) version.py. Do not worry about this unless you really need to know the version.')
