import math
from fastapi.testclient import TestClient
import pytest
from application.main import app
from random import randint
client = TestClient(app)
from application.main2 import return_title

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Hello World"
    
def test_get_title():
    assert return_title() == "Hezz2: Jeu de cartes marocain"


list_of_numbers = [randint(1, 10) for i in range(0, 10)]


@pytest.mark.parametrize('number', list_of_numbers)
def test_return_square_twice(number: int):
    response = client.get(f"/twice/{number}")
    assert response.status_code == 200
    assert response.json() == math.pow(number, 2)*2
