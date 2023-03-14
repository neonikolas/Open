import requests
# GET
status='available'

res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}",headers = {'accept': 'application/json'})
print(res.status_code)
print(res.text)


# POST
BASE_URL = "https://petstore.swagger.io/v2"
new_pet = {
    "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
headers = {
    "Content-Type": "application/json"
}

response = requests.post(f"{BASE_URL}/pet", json=new_pet)
print(response.json())
#
#PUT
BASE_URL = "https://petstore.swagger.io/v2"
pet_update = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
response = requests.put(f"{BASE_URL}/pet", json=pet_update)
print(response.json())
#
# #DELET
BASE_URL = "https://petstore.swagger.io/v2"

response = requests.delete(f"{BASE_URL}/pet/0"
print(response.json())