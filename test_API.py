import pytest
import requests
import json

#API URL
url = "https://127.0.0.1:8181/rests/data/ietf-yang-library:modules-state"

response = requests.get(url,auth=("admin","admin"),headers= {"Content-Type": "application/xml"})

def test_status_code():
    assert response.status_code == 200
    
def test_responsebody():
    json_response = json.loads(response.text)
    assert json_response == "ietf-restconf"

