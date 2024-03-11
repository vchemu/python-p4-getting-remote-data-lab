import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        url = self.url
        response = requests.get(url)
        return response.content

    def load_json(self):
        return json.loads(self.get_response_body())