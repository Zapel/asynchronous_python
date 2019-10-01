import requests


def get_json(url):
    request = requests.get(url)
    response = request.json()
    # print('response: {}'.format(response))
    return response

def get_station(url):
    space_response = get_json(url)
    for key, value in space_response['iss_position'].items():
        if key == 'longitude':
            longitude = value
        if key == 'latitude':
            latitude = value
    print('longitude:{}, latitude:{}'.format(longitude, latitude))
    return longitude, latitude



if __name__ == '__main__':
    url = "http://api.open-notify.org/iss-now.json"

    space_response = get_json(url)
    get_station(url)









