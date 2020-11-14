import json

car = """{ "model": "Civic",
           "make" : "Honda",
           "variants" : ["sedan", "coupe"]
          }"""

# print(car)

car_dict = json.loads(car)
print(type(car))
print(type(car_dict))