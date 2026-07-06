from hello_world import app
from hello_world.formater import get_formatted, SUPPORTED
from flask import request

moje_imie = "Konrad"# noqa
msg = "Hello World!"


@app.route('/')
def index():
    output = request.args.get('output', 'plain')
    return get_formatted(msg, moje_imie, output.lower())


@app.route('/outputs')
def supported_output():
    return ", ".join(SUPPORTED)