import json
import pickle
import os
# Finding a directory with a script.
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


with open("shopping_list.pkl", "rb") as f_pkl, open("shopping_list.json", "r") as f_json:
    pkl = pickle.load(f_pkl)
    json = json.load(f_json)

print("pkl: ", pkl)
print("json: ", json)
