from aprilprocesser import aprilprocesser_app, mongo
from flask import request, jsonify
from ..models.search import Search


@aprilprocesser_app.route('/api/v1/text', methods=['POST'])
def post_text_file():
    text_file = request.form['text_file']
    get_search = Search(text_file).split_sentences()
    save_search = mongo.db.searches
    save_search.insert(
        {'verbs': get_search[-1]['verbs'],
         'nouns': get_search[-1]['nouns'],
         'adjectives': get_search[-1]['adjectives'],
         'pronouns': get_search[-1]['pronouns'],
         'other_words': get_search[-1]['other_words'],
         'total_words': get_search[-1]['total_words']})
    return jsonify(get_search), 201


@aprilprocesser_app.route('/api/v1/text', methods=['GET'])
def get_text_file():
    get_searches = mongo.db.searches
    searches = []
    for search in get_searches.find():
        searches.append({
            'verbs': search['verbs'],
            'adjectives': search['adjectives'],
            'nouns': search['nouns'],
            'pronouns': search['pronouns'],
            'other_words': search['other_words'],
            'total_words': search['total_words']
        })
    return jsonify(searches[-1]), 201
