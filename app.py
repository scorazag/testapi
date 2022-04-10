from flask import Flask
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return "Hola Mundo"

@app.route('/pokemon/<pokemon>', methods=['GET'])
def get_pokemon(pokemon):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    response = requests.get(url)
    return response.json()


if __name__ == '__main__':
    app.run(host='0.0.0.0')

