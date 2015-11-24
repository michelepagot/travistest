
import unittest

from mock import Mock, patch

from module import *

class AccountTest(unittest.TestCase):
    def test_f1(self):
        ret = module_func1()
        self.assertEquals(1, ret)