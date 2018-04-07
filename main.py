# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from algorithms.similarity_algorithms import *
from algorithms.cosine import *
from algorithms.jaccard import *
from algorithms.dice import *
from algorithms.overlap import *

app = Flask(__name__)


def algorithm_factory(checking_method):
    if checking_method is None:
        return None
    elif checking_method == "cos":
        return CosineSim()
    elif checking_method == "cos_stem":
        return CosineSimStem()
    elif checking_method == "cos_stem_stop_rem":
        return CosineSimStemStopwordsRem()
    elif checking_method == "jac":
        return JaccardSim()
    elif checking_method == "jac_stem":
        return JaccardSimStem()
    elif checking_method == "jac_stem_stop_rem":
        return JaccardSimStemStopwordsRem()
    elif checking_method == "dice":
        return DiceSim()
    elif checking_method == "dice_stem":
        return DiceSimStem()
    elif checking_method == "dice_stem_stop_rem":
        return DiceSimStemStopwordsRem()
    elif checking_method == "overlap":
        return OverlapCoefSim()
    elif checking_method == "overlap_stem":
        return OverlapCoefSimStem()
    elif checking_method == "overlap_stem_stop_rem":
        return OverlapCoefSimStemStopwordsRem()
    else:
        return None


def apply_all_available_similarity_checking_methods(text_a, text_b):
    result_list = list()
    methods = [["cos", "Cosine Similarity"],
               ["cos_stem", "Cosine Similarity (stemming is applied)"],
               ["cos_stem_stop_rem", "Cosine Similarity (stemming and stopwords removal are applied)"],
               ["jac", "Jaccard Similarity"],
               ["jac_stem", "Jaccard Similarity (stemming is applied)"],
               ["jac_stem_stop_rem", "Jaccard Similarity (stemming and stopwords removal are applied)"],
               ["dice", "Dice Coefficient"],
               ["dice_stem", "Dice Coefficient (stemming is applied)"],
               ["dice_stem_stop_rem", "Dice Coefficient (stemming and stopwords removal are applied)"],
               ["overlap", "Overlap Coefficient"],
               ["overlap_stem", "Overlap Coefficient (stemming is applied)"],
               ["overlap_stem_stop_rem", "Overlap Coefficient (stemming and stopwords removal are applied)"]
               ]
    for i in methods:
        algorithm = algorithm_factory(i[0])
        result = algorithm.compare(text_a, text_b)
        print(i[0] + " " + str(result))
        result_list.append((i, str(result)))
        # Prevents caching
        del result
        del algorithm

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
                               result=result, result_list=result_list)


if __name__ == "__main__":
    app.run(debug=True)
