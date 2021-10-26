import csv
import json
import pickle

with open("test_1.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(['Model', 'Year', 'Horsepower', 'Engine size'])
    writer.writerow(['80 1.6 Specs', '1989', '69', '1595 cm3 (97.3 cu-in)'])
    writer.writerow(['80 1.6 Specs', '1993', '102', '1595 cm3 (97.3 cu-in)'])
    writer.writerow(['80 1.8 Specs', '1986', '75', '1781 cm3 (108.7 cu-in)'])

with open("test_1.csv", "r") as f:
    reader = csv.reader(f)
    content = list(reader)

with open("test_2.json", "w") as f:
    json.dump(content, f)

with open("test_2.json", "r") as f:
    reader = json.load(f) 
    content = list(reader)

with open("test_3.pickle", "wb") as f:
    pickle.dump(content, f)