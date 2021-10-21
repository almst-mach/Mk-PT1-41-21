import csv
import json
import pickle


with open(r'C:\python\Mk-PT1-41-21\Tasks\Shavlis\Lessons\car.csv') as f:
    f1 = csv.DictReader(f)
    f2 = list(f1)

with open(r'C:\python\Mk-PT1-41-21\Tasks\Shavlis\Lessons\car.json', 'w') as f:
    json.dump(f2, f)

with open(r'C:\python\Mk-PT1-41-21\Tasks\Shavlis\Lessons\car.json') as f:
    f3 = json.load(f)

with open(r'C:\python\Mk-PT1-41-21\Tasks\Shavlis\Lessons\car.pkl', 'wb') as f:
    pickle.dump(f3, f)