# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, jsonify,make_response
from flask_restful import Api, Resource, fields, marshal_with,reqparse
import data_model,madchef_scraping,pizzahut_scraping
import json
app = Flask(__name__)
app.debug=False
api = Api(app)


class FastFood(Resource):
    #@marshal_with(resource_fields)
    def get(self, item, pref_price, location):
        result=data_model.model(pref_price, item, location)
        print(json.dumps(result))
        #return make_response(json.dumps(result), 200)
        return  make_response(jsonify(result), 200)
api.add_resource(FastFood, "/best_deals/<string:item>/<int:pref_price>/<string:location>")

if __name__ == "__main__":
    madchef_scraping.scrap_upload_madchef()
    pizzahut_scraping.scrap_upload_pizzahut()
    app.run()