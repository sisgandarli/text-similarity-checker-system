from flask import Flask, render_template, request
from algorithms.similarity_algorithms import *

app = Flask(__name__)


def algorithm_factory(checking_method):
    if checking_method == "cosine":
        return CosineSimilarityAlgorithm()
    elif checking_method == "jaccard":
        return JaccardSimilarityAlgorithm()
    elif checking_method == "cosine_stemming":
        return CosineSimilarityAlgorithmWithStemming()
    elif checking_method == "jaccard_stemming":
        return JaccardSimilarityAlgorithmWithStemming()
    elif checking_method == "cosine_stemming_stopwords_removed":
        return CosineSimilarityAlgorithmWithStemmingStopwordsRemoved()
    elif checking_method == "jaccard_stemming_stopwords_removed":
        return JaccardSimilarityAlgorithmWithStemmingStopwordsRemoved()
    else:
        return None


def apply_all_available_similarity_checking_methods(text_a, text_b):
    result_list = list()
    methods = ["cosine", "jaccard", "cosine_stemming", "jaccard_stemming", "cosine_stemming_stopwords_removed",
            "jaccard_stemming_stopwords_removed"]
    for i in methods:
        algorithm = algorithm_factory(i)
        result = algorithm.compare(text_a, text_b)
        print(i + " " + str(result))
        result_list.append((i, str(result)))
    return result_list

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

        result_list = apply_all_available_similarity_checking_methods(text_a, text_b)

        return render_template("result.html", text_a=text_a, text_b=text_b, checking_method=checking_method.upper(),
                               result=result, result_list = result_list)


if __name__ == "__main__":
    app.run(debug=True)
