import unittest
import sys
import os

cd = os.path.dirname(__file__)
pd = os.path.join(cd, '..')
sys.path.insert(0, pd)

if __name__ == '__main__':
    load = unittest.TestLoader()
    test = os.path.dirname(__file__)
    x = load.discover(test, pattern='test_*.py')
    rn = unittest.TextTestRunner(verbosity=1)
    result = rn.run(x)
