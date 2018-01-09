from aprilprocesser import aprilprocesser_app
from flask import request, jsonify
from ..models.search import Search


@aprilprocesser_app.route('/api/v1/text', methods=['POST'])
def post_text_file():
    output = request.form['ejemplo']
    the_search = Search(output)
    return jsonify("SERVIDOR = Se termino de hacer el procesamiento de texto ..." + output), 201
