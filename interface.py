from requests import get
from bs4 import BeautifulSoup as BS
from pprint import pprint
from datetime import datetime


class Hook():
    def __init__(self, url: str, filters = {}, *args, **kwargs):
        self.url = url
        self.raw_response = None
        self.bs = BS('','html.parser')
        self._update()
        self.filters = filters
    def _get_raw_html(self):
        return self.raw_response.text
    def _get_raw_response(self):
        return self.raw_response
    def _update(self):
        self.raw_response = get(self.url)
        self.bs = BS(self.raw_response.text, 'html.parser')

    def get_jobs(self):
        raise NotImplementedError("Can't use generic Hook class.")
    def parse_jobs(self):
        raise NotImplementedError("Can't use generic Hook class.")
