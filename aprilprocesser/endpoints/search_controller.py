from aprilprocesser import aprilprocesser_app
from flask import request, jsonify
from ..models.search import Search

output = Search

@aprilprocesser_app.route('/api/v1/text', methods=['POST'])
def post_text_file():
    global output
    output = request.form['ejemplo']
    the_search = Search(output).split_sentences()
    return jsonify(the_search), 201


@aprilprocesser_app.route('/api/v1/text', methods=['GET'])
def get_text_file():
    global output
    the_search = Search(output).get_result()
    return jsonify(the_search), 201
