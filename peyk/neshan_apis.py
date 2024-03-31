import requests

class APIRequest:
    def __init__(self, origin, destination):
        self.origin =  origin
        self.destination = destination 
    

    def is_tehran(self):
        url = f'https://api.neshan.org/v5/reverse?lat={self.origin[0]}&lng={self.origin[1]}'
        url2 = f'https://api.neshan.org/v5/reverse?lat={self.destination[0]}&lng={self.destination[1]}'
        city = (requests.get( url=url, headers={'Api-key' : 'service.0d295e34dd87439ca3a656ea3b87c18a'})).json()['city']
        city2 = (requests.get( url=url2, headers={'Api-key' : 'service.0d295e34dd87439ca3a656ea3b87c18a'})).json()['city']
        if city and city2 == 'تهران':
            return True


    def get_duration(self):
        if self.is_tehran():
            url = f'https://api.neshan.org/v4/direction?type=car&origin={self.origin[0]},{self.origin[1]}&destination={self.destination[0]},{self.destination[1]}'
            duration = requests.get(url=url, headers={'Api-key' : 'service.0d295e34dd87439ca3a656ea3b87c18a'} ).json()["routes"][0]["legs"][0]['duration']['value']
            return duration