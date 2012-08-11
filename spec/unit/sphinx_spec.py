import sys
import os
import fudge

sys.path.insert(0, os.path.abspath('..'))
from flyingsphinx import Sphinx

def test_start():
  api = fudge.Fake('API')
  api.expects('post').with_args('start')
  Sphinx(api).start()

def test_stop():
  api = fudge.Fake('API')
  api.expects('post').with_args('stop')
  Sphinx(api).stop()
