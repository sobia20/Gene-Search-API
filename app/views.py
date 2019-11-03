from flask import request, Response
from app import app, engine
import json


@app.route('/', methods=['GET'])
def index():
    """Displays the URL for navigation"""
    return Response(
        "Go to /searchgene/?name={value}&species={value} to search for genes. <br>" 
        "Go to /swagger for documentation",
        200)


@app.route('/searchgene/', methods=['GET'])
def search():
    """displays gene's stable_id, display_label and species from gene_autocomplete table that match the search or are
    similar """

    def execute_and_print(query):
        val = engine.execute(query)
        list_of_query = []
        for v in val:
            list_of_query.append(dict(v))
        return json.dumps(list_of_query, sort_keys=True, indent=4)

    args = request.args
    if len(args['name']) >= 3:
        query = ''
        if len(args) == 1 and args['name']:
            query = 'select stable_id, display_label, species from gene_autocomplete where display_label like \"{}%%\"'.format(
                args['name'])
        elif args['species']:
            query = 'select stable_id, display_label, species from gene_autocomplete where display_label like \"{}%%\" and species = \"{}\" '.format(
                args['name'], args['species'])
        else:
            return Response("Please provide name and species", status=400)
        list_of_query = execute_and_print(query)
        app.logger.info('sending request to ensembl database')
        return Response(list_of_query, mimetype='application/json')
    else:
        return Response("Length of name is less than 3. Please provide more information.", status=400)


@app.errorhandler(500)
def internal_server_error_handler(error):
    return "Connection timed out. Please try again"
