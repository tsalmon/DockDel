import platform

if platform.python_version() < '2.7':
    import unittest2 as unittest
else:
    import unittest

from os import remove
from tempfile import NamedTemporaryFile

import requests
import responses

from DockDel.essai import MaClasse

class TestMaClasse(unittest.TestCase):
	def test_essai(self):
		t = MaClasse()
		self.assertEqual(t.addition(5, 5), 10)
		print("test_essai")