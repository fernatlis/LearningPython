from flask import Flask, render_template, json, request

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)


@app.route('/signup')
def signup():
    return render_template('signup.html')

# Point your browser to http://localhost:5000/ and you should have the welcome message.
