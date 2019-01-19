from flask import Flask, render_template
from flask_bootstrap import Bootstrap
"""

"""
app = Flask(__name__)
bootstrap = Bootstrap(app)



@app.route("/")
def index():
    return render_template("index.html")

@app.route('/detect-face', methods=['POST'])
def detect_face():
    # TODO:



if __name__=='__main__':
    app.run(debug=True)
