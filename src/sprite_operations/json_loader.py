import json 

def load_shapes():
    with open('assets/shapefile_directions.json') as f:
        return json.load(f)
