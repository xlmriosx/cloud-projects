# Only import libraries
from google.cloud import datastore
import sys
import json
import os

def to_unicode(string):
    return unicode(string, "utf-8")

def get_values_json(jsondata):
    # Getting values of object root
    restaurant_id = jsondata.get("restaurant_id")
    name = jsondata.get("name")
    cuisine = jsondata.get("cuisine")
    borough = jsondata.get("borough")
    address = jsondata.get("address", {})
    # Getting values of object address
    zipcode = address.get("zipcode", '')
    street = address.get("street", '')
    building = address.get("building", '')
    coord = address.get("coord", [0, 0] )
    longitude = coord[0]
    latitude = coord[1]
    return restaurant_id, name, cuisine,borough, zipcode, street, building, longitude, latitude

def set_values_entity(restaurants, restaurant_id, name, cuisine,borough, zipcode, street, building, longitude, latitude):
    # Assign encoded values to key
    restaurants['id'] = to_unicode(restaurant_id)
    restaurants['name'] = to_unicode(name)
    restaurants['cuisine'] = to_unicode(cuisine)
    restaurants['borough'] = to_unicode(borough)
    restaurants['zipcode'] = to_unicode(zipcode)
    restaurants['street'] = to_unicode(street)
    restaurants['building'] = to_unicode(building)
    restaurants['longitude'] = longitude
    restaurants['latitude'] = latitude
    return restaurants

def convert():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    readFile = os.path.join(BASE_DIR, "restaurants.json")
    # Instantiates a client
    datastore_client = datastore.Client()
    # The kind for the new entity
    kind = 'restaurants'
    print ('\n' + 'Convert to Datastore - Please Wait' + '\n')
    
    # Set lines where will be row data
    lines = []
    # Open file restaurants.json
    with open(readFile, "r") as f:
        lines = f.readlines()
    
    # By each line of file we transform data and put it in entity in Datastore
    for line in lines:
        jsondata = json.loads(line)
        # Get values from json
        restaurant_id, name, cuisine,borough, zipcode, street, building, longitude, latitude = get_values_json(jsondata)
        # The Cloud Datastore key for the new entity
        rest_key = datastore_client.key(kind)
        # Prepares the new entity
        restaurants = datastore.Entity(key=rest_key)
        # Set values to entity
        restaurants = set_values_entity(restaurants, restaurant_id, name, cuisine,borough, zipcode, street, building, longitude, latitude)
        # Saves the entity
        datastore_client.put(restaurants)

    print ('\n' + 'Saved Rows to csv' + '\n')

if __name__ == '__main__':
    convert()
