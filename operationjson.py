import json

car = """{ "model": "Civic",
           "make" : "Honda",
           "variants" : ["sedan", "coupe"]
          }"""

# print(car)

car_dict = json.loads(car)
print(type(car))
print(type(car_dict))

print(car_dict)
print(car_dict['variants'])

with open("data_file/currency.json", "r") as json_file:
    data = json.loads(json_file)
    print(data)