from urllib import response
import pytest
import pdb
from app import app
import json

def test_index_route():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Hola Mundo'

def test_pokemon_route():
    response = app.test_client().get('pokemon/ditto')
    assert response.status_code == 200
    my_json = response.data.decode('utf8').replace("'", '"')
    data = json.loads(my_json)
    assert data['forms'][0]['name'] == 'ditto'
    assert data['moves'][0]['move']['name'] == 'transform'



def test_another_pokemon_route():
    response = app.test_client().get('pokemon/charmander')
    assert response.status_code == 200
    my_json = response.data.decode('utf8').replace("'", '"')
    data = json.loads(my_json)
    assert data['forms'][0]['name'] == 'charmander'
    assert data['moves'][0]['move']['name'] == 'mega-punch'