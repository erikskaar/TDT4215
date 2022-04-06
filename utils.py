import json
import os
from typing import Set
import pandas as pd


def load_data(path):
    """
        Load events from files and convert to dataframe.
        Taken from https://github.com/matejast/tdt4215-2022/blob/main/project_example.py
    """
    map_lst = []
    for f in os.listdir(path):
        file_name = os.path.join(path, f)
        if os.path.isfile(file_name):
            for line in open(file_name):
                obj = json.loads(line.strip())
                if not obj is None:
                    map_lst.append(obj)
    return pd.DataFrame(map_lst)

def jaccard_similarity(a: Set, b: Set):
    # calucate jaccard similarity
    intersectionLen = len(a.intersection(b))
    return float(intersectionLen) / float(len(a) + len(b) - intersectionLen)