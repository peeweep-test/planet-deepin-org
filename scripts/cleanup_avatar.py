import os

with open('planet.ini') as inif:
    ini = inif.read()
    for name in os.listdir('static/hackergotchi'):
        if name != 'default.svg' and not name in ini:
            os.remove(f'static/hackergotchi/{name}')
