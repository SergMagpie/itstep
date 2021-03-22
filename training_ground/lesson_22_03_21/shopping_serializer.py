import os
# Finding a directory with a script.
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

import pickle
import json

shoping_list_example = [
{
    "bread": 1.2,
    "milk": 1.6,
    "potato": 0.4,
    "sunflower oil": 2,
    "meat": 2.4
},
{
    "bread": 1.2,
    "milk": 1.6,
    "potato": 0.4,
    "sunflower oil": 2,
    "meat": 2.4,
    "eggs": 0.4,
    "fish": 2.4
}
]
with open("shopping_list.pkl", "wb") as f_pkl, open("shopping_list.json", "w") as f_json:
    pickle.dump(shoping_list_example, f_pkl)
    json.dump(shoping_list_example, f_json)

