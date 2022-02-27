from app import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_get():
    response = client.get("/")
    assert response.status_code == 200 ,'some problem internal'
    assert "text/html" in response.headers['content-type']
    assert response.text != "<h1> hello world </h1>" 
    

def test_post():
    path = "upload/backgrokund.jpg"
    response = client.post("/count_rice",files={'image':open(path,'rb')})
    assert response.status_code == 200 ,'some problem internal'
    assert 'application/json' in response.headers['content-type']


 