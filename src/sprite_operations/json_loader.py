import os
import json

dirname = os.path.dirname(__file__)


def load_shapes():
    with open(os.path.join(dirname, "..", "assets",
                           "shapefile_directions.json"), encoding='utf8') as file:
        return json.load(file)
