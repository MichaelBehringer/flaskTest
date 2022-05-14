from flask import Flask
from flask import jsonify
import random
import _thread

#pip install Flask

values = [0] * 500
counter = 0

rest = Flask(__name__)

def prompt():
    while 1:
        global values
        global counter
        newValue = random.randint(0,999999)
        values[counter] = newValue
        counter = counter + 1
        if(counter == 500):
            counter = 0

@rest.route('/', methods=['GET'])
def getVersion():
    return jsonify(result=values)

if __name__ == '__main__':
    _thread.start_new_thread( prompt, () )
    rest.run(port=2506)