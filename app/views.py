from flask import request, Response, jsonify
from app import app,  metadata, engine
from sqlalchemy  import Table
import json 


@app.route('/searchgene/', methods=['GET'])
def index():
	"""displays gene's stable_id, display_label and species from
	 gene_autocomplete table that match the search or are similar """

	def executeAndPrint(query):
		# print(query)
		val = engine.execute(query)
		# print(val)
		list_of_query = []
		for v in val:
			list_of_query.append(dict(v))
		print(list_of_query)
		return json.dumps(list_of_query,sort_keys = True, indent = 4)
		
	if request.args and request.args['name']:
		args = request.args
		print(args['name'],  len(args))
		if len(args['name'])>=3:
			query=''
			if len(args)==1 and args['name']:
				query = 'select stable_id, display_label, species from gene_autocomplete where display_label like \"%%{}%%\"'.format(args['name'])
			elif args['species']:
				query = 'select stable_id, display_label, species from gene_autocomplete where display_label like \"%%{}%%\" and species = \"{}\" '.format(args['name'], args['species'])				
			else:
				return Response("Please provide name and species", status = 400)
			list_of_query = executeAndPrint(query)
			return Response(list_of_query, mimetype='application/json')
		else:
			return Response("Length of name is less than 3. Please provide more information.", status=400)
	else:
		return Response("Please enter name and species to search in Ensembl database", status=400)
