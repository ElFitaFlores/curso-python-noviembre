# API - stateless
# request
# URL - dominio - https://google.com - https://189.205.65.69
# URL - path - https://google.com/photos
# método - GET - POST - PUT - DELETE 
# body - {
#   "name": "Rafael",
#   "email": "email@ejemplo.com"
# }
# headers - Authorization: abc-123, Content-Type: application/jpg, Accept: application/excel
# Path parameters /photos/1
# Query params /friends?gender=male&adults=yes

# endpoint 
# response
# Body 
# Headers
# Códigos HTTP - 100 200 300 400

import requests

response = requests.get('https://swapi.dev/api/people', params={'page': 2})
print(response)
print(response.status_code)
#print(response.content)
print(response.headers)
data = response.json()
print(data['results'][0]['name'])
