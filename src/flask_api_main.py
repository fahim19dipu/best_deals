# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 01:16:22 2022

@author: fahim
"""
from flask import Flask, jsonify,make_response
from flask_restful import Api, Resource, fields, marshal_with,reqparse
import data_model,madchef_scraping,pizzahut_scraping
import json
app = Flask(__name__)
app.debug=False
api = Api(app)
################################################## resourse field for serialzation
food_item_fields = {}
food_item_fields['item name'] = fields.String(attribute='item name')
food_item_fields['catagory'] = fields.String(attribute='catagory')
food_item_fields['short_Description'] = fields.String(attribute='description')
food_item_fields['price'] = fields.Integer(attribute='price')
#food_item_fields['Resutant Name'] = fields.String(attribute='')

address_fields = {}
address_fields['branch_name'] = fields.String(attribute='branch_name')
address_fields['address'] = fields.String(attribute='address')
address_fields['phone'] = fields.String(attribute='phone')

resource_fields = {}
resource_fields['item_list'] = fields.List(fields.Nested(food_item_fields))
resource_fields['madChef_loaction'] = fields.List(fields.Nested(address_fields))
resource_fields['pizzahut_locations'] = fields.List(fields.Nested(address_fields))
##########################################      API class
class FastFood(Resource):
    #@marshal_with(resource_fields)
    def get(self, item, pref_price, location):
        result=data_model.model(pref_price, item, location)     ##### calling data model
        print(json.dumps(result))
        return make_response(json.dumps(result), 200) 
        #return jsonify(result), 200
api.add_resource(FastFood, "/best_deals/<string:item>/<int:pref_price>/<string:location>")

if __name__ == "__main__":
    madchef_scraping.scrap_upload_madchef()                     ####  callinng madchef scraper
    pizzahut_scraping.scrap_upload_pizzahut()                   ####  caliing pizzahut scraper
    app.run()                                                   ####  Run API
