import pytest
from app import app

@pytest.fixture
def Request:
    app.config['TESTING'] = True
    with app.Request() as Request:
        yield Request

def testEndpoint(Request):
    response = Request.get('/')
    assert response.status_code == 200
    assert b'is the current date and time.' in response.data
