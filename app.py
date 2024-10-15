from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
  return f"<h1><center> Hello World app! Version  3 {hostname}<center><h1>"

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=5000)
  hostname = os.getenv('HOSTNAME',none)
