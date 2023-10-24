import requests, json


def format_API_call(resource_type, params):
    # basic api call format
    # https://api.harvardartmuseums.org/RESOURCE_TYPE?apikey=YOUR_API_KEY
    api_key = '851ef57f-d388-4e2e-9c7b-5a7e1c948c9a'
    base_url = 'https://api.harvardartmuseums.org/'
    params = params
    API_call = f"{base_url}{resource_type}?apikey={api_key}{params}"
    return API_call


sample_call = format_API_call('culture', '&sort=random&size=5')
request = requests.get(sample_call)
print(json.dumps(request.json(), indent=4, sort_keys=True))




