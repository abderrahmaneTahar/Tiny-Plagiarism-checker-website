from flask import Flask, jsonify, render_template, request
import plagrism_check 


app = Flask(__name__)


@app.route("/",method=["GET","POST"])
def index():
    if request.method == "POST":
        word = request.files['word']
        return plagrism_check.process_file(word)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)