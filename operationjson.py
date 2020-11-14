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
    data = json.load(json_file)
    print(data)

currency = { "Country": "India", "Currency": "Rupee"}
json_var = json.dumps(currency)
print(json_var)

print(type(json_var))

with open("data_file/currency.json", "w") as json_file:
    json_file.write(json_var)
    print(type(json_file))

with open("data_file/currency.json", "r") as json_file:
    data = json.load(json_file)
    print(data)