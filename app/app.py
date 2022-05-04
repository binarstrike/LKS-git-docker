from flask import Flask

app = Flask(__name__)

home=("""
<h1>Hello, World!</h1>
<h2>OK</h2>
""")


@app.route("/home")
def home_page():
    return home
