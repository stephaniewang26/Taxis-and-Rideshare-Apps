import json

# Create a list of all the JSON files that you want to combine.
json_files = []
ending = "_yellowtaxi.json"

for i in range (2016,2023):
    json_files.append(str(i)+ending)

# Create an empty list to store the Python objects.
python_objects = []

# Load each JSON file into a Python object.
for json_file in json_files:
    with open(json_file, "r") as f:
        python_objects.append(json.load(f))

# Dump all the Python objects into a single JSON file.
with open("combined.json", "w") as f:
    json.dump(python_objects, f, indent=4)