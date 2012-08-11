import sys
import os
import fudge

sys.path.insert(0, os.path.abspath('..'))
from flyingsphinx import Sphinx

@fudge.test
def test_start():
  api = fudge.Fake('API')
  api.expects('post').with_args('start')
  Sphinx(api).start()

@fudge.test
def test_stop():
  api = fudge.Fake('API')
  api.expects('post').with_args('stop')
  Sphinx(api).stop()

@fudge.test
def test_index_start():
  api = fudge.Fake('API')
  api.provides('get').returns({'status': 'FINISHED', 'log': 'indexer output'})

  api.expects('post').with_args('indices', {'indices': ''})\
    .returns({'id': '55'})

  Sphinx(api).index()

@fudge.test
def test_index_checks():
  api = fudge.Fake('API')
  api.provides('post').returns({'id': '55'})

  api.expects('get').with_args('indices/55').returns({
    'status': 'FINISHED',
    'log':    'indexer output'
  })

  Sphinx(api).index()

@fudge.patch('time.sleep')
def test_index_checks_more_than_once(sleep):
  api = fudge.Fake('API')
  api.provides('post').returns({'id': '55'})
  api.provides('get').with_args('indices/55').returns({'status': 'PENDING'})\
    .next_call().returns({'status': 'FINISHED', 'log': 'indexer output'})

  sleep.expects_call().with_args(3)

  Sphinx(api).index()

@fudge.patch('sys.stdout.write')
def test_index_prints_result(printer):
  api = fudge.Fake('API')
  api.provides('post').returns({'id': '55'})
  api.provides('get').with_args('indices/55').returns({
    'status': 'FINISHED',
    'log':    'indexer output'
  })

  printer.expects_call().with_args('indexer output\n')

  Sphinx(api).index()

@fudge.patch('sys.stdout.write')
def test_index_prints_result(printer):
  api = fudge.Fake('API')
  api.provides('post').returns({'id': '55'})
  api.provides('get').with_args('indices/55').returns({'status': 'FAILED'})

  printer.expects_call().with_args('Index request failed.\n')

  Sphinx(api).index()
