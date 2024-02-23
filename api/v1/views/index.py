#!/usr/bin/python3
"""
index
"""


from models import storage
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def ok():
        """status ok"""
        return (jsonify(status="ok"))
