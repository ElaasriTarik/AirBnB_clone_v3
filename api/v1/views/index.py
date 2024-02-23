#!/usr/bin/python3
"""
index
"""


from api.v1.views import app_views
import jsonify


@app_views.route('/status')
def ok():
	"""status ok"""
	return (jsonify({'status': 'ok'}))
