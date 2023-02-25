

#  ⛵ Simple way to upload data in format JSON to Datastore from GCP.

---

## 🔗Related content  
### You can find post related in:
👨‍💻[DEV](https://dev.to/xlmriosx/how-upload-data-in-format-json-to-datastore-from-gcp-20no) 

### You can connect with me in:
🧬[LinkedIn](https://www.linkedin.com/in/xlmriosx/) 

--- 

### Resume 🧾

All this blog is using shell.

We will upload data to Datastore we can made this with Cloud SDK or directly from shell in GCP.

We will create a script in json_to_datastore.py to upload data from restaurants.json to Datastore.

For more information and potential of this, click [here](https://cloud.google.com/datastore).

---

### 1st - Create a program python ✍️

I use following command:

```
touch json_to_datastore.py
```

---

### 2nd - Write code to do transforms 🧵

Open IDE(I use vi) and put the following script

```
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
```

---

### 3rd - Run script 🙈

We need restaurants.json is in same path of script.

We run script with following command:

```
python3 json_to_datastore.py
```

UALAAAAA! 🎩🪄
You now have data in your instance of Datastore...

---

### 4th - Say thanks, give like and share if this has been of help/interest 😁🖖

---
