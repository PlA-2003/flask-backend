import pytest     
from app import app
import json

client = app.test_client()

def test_get_version():
    response = client.get('/get_version')
    assert response.status_code == 200
    response_json = json.loads(response.data)
    assert response_json["version"] == "1.0.0"

def test_check_prime_prime():
    response = client.get('/check_prime/7')
    assert response.status_code == 200
    response_json = json.loads(response.data)
    assert response_json["is_prime"] is True
    assert response_json["number"] == 7

def test_check_prime_non_prime():
    response = client.get('/check_prime/8')
    assert response.status_code == 200
    response_json = json.loads(response.data)
    assert response_json["is_prime"] is False
    assert response_json["number"] == 8

def test_check_prime_negative():
    response = client.get('/check_prime/-5')
    assert response.status_code == 400
    response_json = json.loads(response.data)
    assert response_json["error"] == "Negative numbers are not allowed"

def test_check_prime_invalid_input():
    response = client.get('/check_prime/abc')
    assert response.status_code == 400
    response_json = json.loads(response.data)
    assert response_json["error"] == "Invalid number"

def test_check_prime_zero():
    response = client.get('/check_prime/0')
    assert response.status_code == 200
    response_json = json.loads(response.data)
    assert response_json["is_prime"] is False
    assert response_json["number"] == 0

def test_check_prime_two():
    response = client.get('/check_prime/2')
    assert response.status_code == 200
    response_json = json.loads(response.data)
    assert response_json["is_prime"] is True
    assert response_json["number"] == 2

def test_check_prime_large_prime():
    response = client.get('/check_prime/101')
    assert response.status_code == 200
    response_json = json.loads(response.data)
    assert response_json["is_prime"] is True
    assert response_json["number"] == 101

def test_check_prime_large_non_prime():
    response = client.get('/check_prime/200')
    assert response.status_code == 200
    response_json = json.loads(response.data)
    assert response_json["is_prime"] is False
    assert response_json["number"] == 200

def test_check_prime_one():
    response = client.get('/check_prime/1')
    assert response.status_code == 200
    response_json = json.loads(response.data)
    assert response_json["is_prime"] is False
    assert response_json["number"] == 1

