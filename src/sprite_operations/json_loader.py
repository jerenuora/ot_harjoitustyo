"""
Form a filepath and load a json
"""

import os
import json

dirname = os.path.dirname(__file__)


def load_shapes():
    """
    Loads the json and reads the file to a usable format

    Returns:
        file: the file
    """
    with open(os.path.join(dirname, "..", "assets",
                           "shapefile_directions.json"), encoding='utf8') as file:
        return json.load(file)
