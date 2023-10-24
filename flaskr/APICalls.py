import requests

class API_Caller():
    def __init__(self):
        pass

    def format_API_call(self, resource_type, params):
        # basic api call format: https://api.harvardartmuseums.org/RESOURCE_TYPE?apikey=YOUR_API_KEY
        api_key = '851ef57f-d388-4e2e-9c7b-5a7e1c948c9a'
        base_url = 'https://api.harvardartmuseums.org/'
        params = params
        API_call = f"{base_url}{resource_type}?apikey={api_key}{params}"
        return API_call
    
    def send_call(self, resource_type, params):
        # sample_call = self.format_API_call('image', '&sort=random&size=5')
        call_txt = self.format_API_call(resource_type, params)
        request = requests.get(call_txt)
        return(request.json())
    
    def get_image_url(self):
        # used to get a URL from API in get_image()
        return self.send_call('image', '&sort=random&size=5')["records"][0]["baseimageurl"]
    
    def get_image(self):
        # sets up image to be displayed
        response = requests.get(self.get_image_url())
        return response



def test():
    api = API_Caller()
    call = api.send_call('image', '&sort=random&size=5')
    print(call["records"][0]["baseimageurl"])
    print(api.get_image())

    


if __name__ == '__main__':
    test()