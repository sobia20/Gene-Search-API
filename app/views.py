from flask import request, Response
from app import app, engine
import json


@app.route('/', methods=['GET'])
def index():
	"""Displays the URL for navigation"""
	return Response("Please navigate to /searchgene to search for genes and to /swagger to see documentation", 200)


@app.route('/searchgene/', methods=['GET'])
def search():
	"""displays gene's stable_id, display_label and species from
	 gene_autocomplete table that match the search or are similar """

	def execute_and_print(query):
		# print(query)
		val = engine.execute(query)
		# print(val)
		list_of_query = []
		for v in val:
			list_of_query.append(dict(v))
		print(list_of_query)
		return json.dumps(list_of_query, sort_keys=True, indent=4)

	print(request.args)
	args = request.args
	if len(args['name']) >= 3:
		query = ''
		if len(args) == 1 and args['name']:
			query = 'select stable_id, display_label, species from gene_autocomplete where display_label like \"%%{}%%\"'.format(args['name'])
		elif args['species']:
			query = 'select stable_id, display_label, species from gene_autocomplete where display_label like \"%%{}%%\" and species = \"{}\" '.format(args['name'], args['species'])
		else:
			return Response("Please provide name and species", status=400)
		list_of_query = execute_and_print(query)
		return Response(list_of_query, mimetype='application/json')
	else:
		return Response("Length of name is less than 3. Please provide more information.", status=400)


