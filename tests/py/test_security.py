from __future__ import unicode_literals
from pytest import yield_fixture

from aspen.testing.client import Client
from inside_gratipay.main import website

@yield_fixture
def client():
    client = Client(www_root='www', project_root='.')
    client._website = website
    yield client

def test_disallowed_methods(client):
    for disallowed in ['TRACE', 'trAce', 'DELETE', 'PUT', 'OPTIONS', 'JUNK']:
        response = client.hxt(disallowed, '/')
        assert response.code == 405

def test_allowed_methods(client):
    for allowed in ['GET', 'gEt', 'POST', 'HEAD']:
        response = client.hit('GET', trace='/')
        assert response.code == 200
