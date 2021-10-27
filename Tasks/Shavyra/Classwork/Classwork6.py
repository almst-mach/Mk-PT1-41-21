import csv
import json
import pickle

with open("auto_settings.csv", "w", newline = "") as f:
    writer = csv.writer(f)
    writer.writerow(['Model', 'Year', 'Horsepower', 'Engine Size'])
    writer.writerow(['80 1.6 Specs', '1989', '69', '1595 cm3'])
    writer.writerow(['80 1.6 Specs', '1993', '102', '1595 cm3'])
    writer.writerow(['80 1.8 Specs', '1986', '75', '1781 cm3'])

f = open("auto_settings.csv", 'r')
reader = csv.DictReader(f, fieldnames = ('Model', 'Year', 'Horsepower', 'Engine Size'))
out = json.dumps([row for row in reader])

print(out)

with open("auto_settings_js.json", 'w') as f:
    json.dump(out, f)

with open("auto_settings_pickle.pickle", 'wb') as f:
    pickle.dump(out, f)