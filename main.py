from flask import Flask, render_template, request
from algorithms.similarity_algorithms import *

app = Flask(__name__)


def algorithm_factory(checking_method):
    if checking_method == "cosine":
        return CosineSimilarityAlgorithm()
    elif checking_method == "jaccard":
        return JaccardSimilarityAlgorithm()
    else:
        return None


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        text_a = request.form["text_a"]
        text_b = request.form["text_b"]
        checking_method = request.form['checking-method']

        algorithm = algorithm_factory(checking_method)
        result = algorithm.compare(text_a, text_b)

        return render_template("result.html", text_a=text_a, text_b=text_b, checking_method=checking_method.upper(),
                               result=result)


if __name__ == "__main__":
    app.run(debug=True)
