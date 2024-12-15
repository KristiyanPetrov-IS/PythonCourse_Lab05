import json
import csv
import sys

def print_json(data):
    print(json.dumps(data))

def print_csv(data):
    writer = csv.DictWriter(sys.stdout, fieldnames=["title", "rating"])
    writer.writeheader()
    writer.writerows(data)