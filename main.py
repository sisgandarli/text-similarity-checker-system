# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from algorithms.similarity_algorithms import *
from algorithms.ann import *
from algorithms.cosine import *
from algorithms.jaccard import *
from algorithms.dice import *
from algorithms.overlap import *
from algorithms.ann_50_50 import *
from algorithms.ann_random_data import *
from algorithms.mean import *

app = Flask(__name__)

method_names = {}
method_names["cos"] = "Cosine Similarity"
method_names["cos_stem"] = "Cosine Similarity (stemming is applied)"
method_names["cos_stem_stop_rem"] = "Cosine Similarity (stemming and stopwords removal are applied)"
method_names["jac"] = "Jaccard Similarity"
method_names["jac_stem"] = "Jaccard Similarity (stemming is applied)"
method_names["jac_stem_stop_rem"] = "Jaccard Similarity (stemming and stopwords removal are applied)"
method_names["dice"] = "Dice Coefficient"
method_names["dice_stem"] = "Dice Coefficient (stemming is applied)"
method_names["dice_stem_stop_rem"] = "Dice Coefficient (stemming and stopwords removal are applied)"
method_names["overlap"] = "Overlap Coefficient"
method_names["overlap_stem"] = "Overlap Coefficient (stemming is applied)"
method_names["overlap_stem_stop_rem"] = "Overlap Coefficient (stemming and stopwords removal are applied)"
method_names["ann"] = "Artificial Neural Network (default news dataset)"
method_names["ann_50x50"] = "Artificial Neural Network (news dataset with 50% positive and 50% negative examples)"
method_names["ann_random_data"] = "Artificial Neural Network (random dataset with 50% positive and 50% negative examples)"
method_names["mean"] = "Mean Value of Results of Applying Term-based Similarity Checking Algorithms"

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
    elif checking_method == "ann":
        return ANN()
    elif checking_method == "ann_50x50":
        return ANN_50X50()
    elif checking_method == "ann_random_data":
        return ANN_RandomData()
    elif checking_method == "mean":
        return Mean()
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

        checking_method_name = method_names[checking_method]

        algorithm = algorithm_factory(checking_method)
        result = algorithm.compare(text_a, text_b)

        # result_list = apply_all_available_similarity_checking_methods(text_a, text_b)

        return render_template("result.html", text_a=text_a, text_b=text_b, checking_method=checking_method_name.upper(),
                               result=result)


if __name__ == "__main__":
    app.run(debug=True)
