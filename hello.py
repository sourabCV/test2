# import sys
#
# def hello():
#     print(sys.argv)
#
#
# if __name__ == "__main__":
#     hello()

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

app.run(port = 5001,debug=False)