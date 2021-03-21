from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
  return render_template("home.html")

@app.route('/aduso')
def aduso():
  return render_template("aduso.html")

@app.route('/layout')
def layout():
  return render_template("layout.html")

if __name__ == "__main__":
  app.run(debug = True)