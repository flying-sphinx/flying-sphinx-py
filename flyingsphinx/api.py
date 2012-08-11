import requests
import os
import flyingsphinx

class API(object):
  def __init__(self, identifier = None, api_key = None):
    self.identifier = identifier or os.environ['FLYING_SPHINX_IDENTIFIER']
    self.api_key    = api_key    or os.environ['FLYING_SPHINX_API_KEY']

  def post(self, path, body={}):
    requests.post(
      'https://flying-sphinx.com/api/my/app/' + path,
      body, self._headers()
    )

  def _headers(self):
    return {
      'Accept':                  'application/vnd.flying-sphinx-v3+json',
      'X-Flying-Sphinx-Token':   ('%s:%s' % (self.identifier, self.api_key)),
      'X-Flying-Sphinx-Version': ('%s+python' % flyingsphinx.__version__)
    }
