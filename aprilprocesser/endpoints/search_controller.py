from aprilprocesser import aprilprocesser_app, mongo
from flask import request, jsonify
from ..models.search import Search

output = Search


@aprilprocesser_app.route('/api/v1/text', methods=['POST'])
def post_text_file():
    global output
    output = request.form['ejemplo']
    get_search = Search(output).split_sentences()
    save_search = mongo.db.searches
    print("\n")
    print(get_search)
    print(get_search[-1])
    print("\n")
    save_search.insert(
        {'verbs': get_search[-1]['verbs'], 'nouns': get_search[-1]['nouns'], 'adjectives': get_search[-1]['adjectives'],
         'pronouns': get_search[-1]['pronouns'], 'other_words': get_search[-1]['other_words'],
         'total_words': get_search[-1]['total_words']})
    return jsonify(get_search), 201


@aprilprocesser_app.route('/api/v1/text', methods=['GET'])
def get_text_file():
    global output
    the_search = Search(output).get_result()
    return jsonify(the_search), 201
