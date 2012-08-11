import sys
import os
import fudge

sys.path.insert(0, os.path.abspath('..'))
from flyingsphinx import Configuration

def test_configuration_upload():
  api = fudge.Fake('API')
  api.expects('put').with_args('/', {'configuration': 'provided content'})
  Configuration(api).upload('provided content')

@fudge.patch('__builtin__.open')
def test_configuration_upload_from_file(fake_open):
  api       = fudge.Fake('API')
  conf_file = fudge.Fake('File')
  fake_open.is_callable().calls(lambda path: conf_file)
  conf_file.provides('read').returns('content in file')

  api.expects('put').with_args('/', {'configuration': 'content in file'})

  Configuration(api).upload_from_file('/path/to/file')
