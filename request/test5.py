import requests
from getpass import getpass
from requests.auth import HTTPBasicAuth

username = 'Zapel'
password = 'fisher1706'

# response = requests.get('https://api.github.com/user', auth=('username', getpass()))
# print(response)

# response1 = requests.get('https://api.github.com/user', auth=HTTPBasicAuth('Zapel', getpass()))
# print(response1)

response2 = requests.get('https://api.github.com/user', auth=(username, password))
print(response2)

with requests.Session() as session:
    session.auth = (username, password)
    response = session.get('https://api.github.com/user')

    print(response.headers)
    print(response.json())
