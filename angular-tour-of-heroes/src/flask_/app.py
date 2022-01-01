from flask import Flask, Response, json
app = Flask(__name__)

@app.route('/api/heroes', methods=['GET'])
def heroes():
    heroes = [
        { "id": 11, "name": 'Dr Nice' },
        { "id": 12, "name": 'Narco' },
        { "id": 13, "name": 'Bombasto' },
        { "id": 14, "name": 'Celeritas' },
        { "id": 15, "name": 'Magneta' },
        { "id": 16, "name": 'RubberMan' },
        { "id": 17, "name": 'Dynama' },
        { "id": 18, "name": 'Dr IQ' },
        { "id": 19, "name": 'Magma' },
        { "id": 20, "name": 'Tornado' }
    ];
    # https://flask.palletsprojects.com/en/2.0.x/api/#flask.Response
    resp = Response(
        response=json.dumps(heroes),
        content_type="application/json",
        headers=[('Access-Control-Allow-Origin', '*')],
        )
    return resp


if __name__ == "__main__":
    app.run(host='0.0.0.0')
