from flask import Flask, render_template, jsonify, request
import requests
import os

static_dir = str(os.path.abspath(os.path.join(__file__, "..", "frontend")))
app = Flask(__name__, static_folder=static_dir, static_url_path="", template_folder=static_dir)


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/api/search', methods=['GET'])
def autocomplete():
    """Seqwa Search API"""
    response = requests.get('https://www.seqwa.com/api/v1/search', params={
        "index": 'cde1d8e5-f0af-4498-801d-3ff82acec9c6', # Replace with your Index Id
        "query": request.args.get('query'),
        "context": request.args.get('context'),
        "type": request.args.get('type'),
        "highlightField": 'title', # Include the field that needs to be highlighted for the suggestions. It is optional. By not setting this field you may end up with results from any field.
        "fields": 'title,price,image,link',
        "maxResults": 200,
    }, headers={'Content-Type': 'application/json', 'seqwa-api-key': '87b622a4a8829636149d4c90d748274b2287b022'})

    return jsonify(response.json())


if __name__ == '__main__':
    app.run()
