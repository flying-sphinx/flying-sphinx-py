import sys
import os
import fudge
import requests

sys.path.insert(0, os.path.abspath('..'))
from flyingsphinx import API

@fudge.patch('requests.get')
def test_get(get_method):
  get_method.expects_call().with_args(
    'https://flying-sphinx.com/api/my/app/path', {'id': '55'}, {
      'Accept': 'application/vnd.flying-sphinx-v3+json',
      'X-Flying-Sphinx-Token': 'abc:123',
      'X-Flying-Sphinx-Version': '0.0.1+python'
    }
  )

  api = API('abc', '123')
  api.get('path', {'id': '55'})

@fudge.patch('requests.post')
def test_post(post_method):
  post_method.expects_call().with_args(
    'https://flying-sphinx.com/api/my/app/start', {}, {
      'Accept': 'application/vnd.flying-sphinx-v3+json',
      'X-Flying-Sphinx-Token': 'abc:123',
      'X-Flying-Sphinx-Version': '0.0.1+python'
    }
  )

  api = API('abc', '123')
  api.post('start')

@fudge.patch('requests.put')
def test_put(put_method):
  put_method.expects_call().with_args(
    'https://flying-sphinx.com/api/my/app/path', {'foo': 'bar'}, {
      'Accept': 'application/vnd.flying-sphinx-v3+json',
      'X-Flying-Sphinx-Token': 'abc:123',
      'X-Flying-Sphinx-Version': '0.0.1+python'
    }
  )

  api = API('abc', '123')
  api.put('path', {'foo': 'bar'})
