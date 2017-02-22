from flask import Flask
import tensorflow as tf

app = Flask(__name__)

@app.route("/")
def hello():
   return "Tensorflow version {}".format(tf.__version__)

if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True, port=80)