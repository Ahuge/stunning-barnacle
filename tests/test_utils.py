from io import StringIO
from functools import wraps
import sys
from time import time
import unittest


__out = None


def redirect_stdout(replacement=None):
    global __out
    __out = sys.stdout
    sys.stdout = replacement or StringIO()
    yield __out
    sys.stdout = __out


def _get_out():
    return __out or sys.stdout


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        _get_out().write(
            "\nTest :%r took: %2.4f sec\n"
            % (f.__name__, te-ts)
        )
        return result
    return wrap


class BaseTimingTest(unittest.TestCase):
    timing = timing

    def setUp(self):
        self.redr = next(redirect_stdout())

    def tearDown(self):
        next(redirect_stdout(self.redr))
