import json

#https://medium.com/@abdelfatahmennoun4/how-to-combine-multiple-json-files-into-a-single-json-file-c2ed3dc372c2
# Create a list of all the JSON files that you want to combine.
json_files = []
starting = "data/yearly_yellowtaxi_full_json/"
ending = "_yellowtaxi.json"

for i in range (2016,2023):
    json_files.append(starting+str(i)+ending)

print(json_files)

# Create an empty list to store the Python objects.
python_objects = {}

year = 2015
# Load each JSON file into a Python object.
for json_file in json_files:
    year += 1
    with open(json_file, "r") as f:
        python_objects[year] = (json.load(f))

# Dump all the Python objects into a single JSON file.
with open("combined.json", "w") as f:
    json.dump(python_objects, f, indent=4)