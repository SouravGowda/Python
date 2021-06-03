import requests
import json

baseUrl = 'https://api.openweathermap.org/data/2.5/forecast'
parameters = {'APPID': '5eaf06e5c10e3a48e83840b895a6693f','q':'Koppa'}
response = requests.get(baseUrl,params=parameters)
# print(response.content)



content = response.content
info = json.loads(content)
# print(type(info))
# print(info)

item = info["list"]
itemInfo = item[0]
title = itemInfo["weather"]
storeInfo = title[0]
product = storeInfo['main']
print(product)

res = list(title[0].keys())[1]
res = next(iter(title[0]))
# print((res))

values_view = title[0].values()
values_ite = iter(values_view)
first_value = next(values_ite)
# print(res + ':' + first_value)