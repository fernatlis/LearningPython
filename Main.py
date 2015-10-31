from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    print("inside main")
    return render_template('index.html')


@app.route("/main")
def home():
    return render_template('index.html')


@app.route('/signup')
def signup():
    print("inside signup")
    return render_template('signup.html')

if __name__ == "__main__":
    app.run(debug=True)


# Point your browser to http://localhost:5000/ and you should have the welcome message.
