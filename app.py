
from flask import Flask, request
import os
import random
import requests

app = Flask(__name__)

@app.route("/")
def home():
    data = requests.get("https://rickandmortyapi.com/api/character")
    data = data.json()
    _str = ""
    _list = []
    for car in data["results"]:
        _list.append(
            {
                "name": car["name"],
                "image": car["image"]
            }
        )
    numero = random.randint(1,(len(_list)-1))
    _dic=_list[numero]

    return '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rick And Morty</title>
</head>
<body>
    <div class="card">
        <img src="'''+_dic['image']+'''" class="imagen">
        <h1 class="name">'''+_dic['name']+'''</h1>
        <p>Actualiza para un personaje diferente </p>
    </div>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Oswald&family=Roboto:wght@300&display=swap');
        body {
            font-family: 'Roboto', sans-serif;
            display: flex;
            padding: 20px 0;
            background-color: #AEE6E3
        }
        h1 {
            font-family: 'Oswald', sans-serif;
            margin: 0;
            padding: 5px;
            font-size: 60px;
        }
        .imagen {
            width: 100%;
            height: 50vh;
            object-fit: fill;
            margin: 0 auto;
            border-radius: 40px;
        }
        .card {
            text-align: center;
            padding: 25px;
            border-radius: 40px;
            margin: auto;
            background-color: #DBD6D0;
            box-shadow: 0px 58px 86px -64px rgba(0, 0, 0, 0.75);
        }
    </style>
</body>
</html>
    '''

if __name__ == '__main__':
    app.run(debug=True, port=8000)
