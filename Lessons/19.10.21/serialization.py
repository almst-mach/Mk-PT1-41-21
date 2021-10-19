import json

x = """
{
  "width": 500,
  "height": 500,
  "resolution": 96,
  "quality": 96,
  "settings": [
    {
      "filename": "_preview1.jpg",
      "seek": 10
    },
    {
      "filename": "_preview2.jpg",
      "seek": 35
    },
    {
      "filename": "_preview3.jpg",
      "seek": 70
    },
    {
      "filename": "_preview4.jpg",
      "seek": 95
    }
  ]
}
"""

image_prop = json.loads(x)
print(type(image_prop))
print(image_prop["settings"][0]["filename"])

with open("test.json", "w") as f:
    json.dump(image_prop, f)