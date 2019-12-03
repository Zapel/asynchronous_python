import requests

response = requests.post('https://httpbin.org/post', json={'key':'value'})
json_response = response.json()



# print(response)
# print(response.headers)
# print(response.content)
# print(json_response)
print(json_response['headers'])
# print(json_response['data'])
# print(json_response['headers']['Content-Type'])
print(response.request)
print(response.request.headers)
print(response.request.url)
print(response.request.body)
