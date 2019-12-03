import requests
from requests.exceptions import HTTPError

# response = requests.get('https://api.github.com')
# print(response.status_code)

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)
        response.raise_for_status()
        # print(response)
        # print(response.content)
        # print(response.status_code)
        # print(response.text)
        # print(type(response.text))
        print(response.json())
        print(response.json().keys())
        print(response.headers)

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')