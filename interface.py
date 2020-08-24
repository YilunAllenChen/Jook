from requests import get
from bs4 import BeautifulSoup as BS
from pprint import pprint
from datetime import datetime


class Hook():
    def __init__(self, url: str, *args, **kwargs):
        self.url = url

        self.raw_response = None
        self.bs = BS('','html.parser')

        self.update()
    def get_raw_html(self):
        return self.raw_response.text
    def get_raw_response(self):
        return self.raw_response
    def update(self):
        self.raw_response = get(self.url)
        self.bs = BS(self.raw_response.text, 'html.parser')


    def get_jobs(self):
        raise NotImplementedError("Can't use generic Hook class.")
    def parse_jobs(self):
        raise NotImplementedError("Can't use generic Hook class.")




class Hook_Google_X(Hook):
    def __init__(self, *args, **kwargs):
        super().__init__(url='https://x.company/careers-at-x/', *args, **kwargs)
    def get_jobs(self):
        return self.bs.findAll('li',attrs={'class': 'job-listing js-job-listing -visible'})
    
    def get_titles(self):
        return [job.find('h4',attrs={'class': 'job-title'}).getText() for job in self.get_jobs()]

    def parse_jobs(self):
        jobs_dict = [{
            'title': job.find('h4',attrs={'class': 'job-title'}).getText(),
            'link': 'https://x.company/' + job.find('a', {'class': 'job-link ak-update-params'}).get('href'),
            'location': job.find('p', {'class': 'job-location'}).getText(),
            'date_updated': datetime.fromisoformat(job.get('data-updated'))
        } for job in self.get_jobs()]
        return jobs_dict

class Hook_Google(Hook):
    def __init__(self, *args, **kwargs):
        super().__init__(url='https://careers.google.com/jobs/results/?company=Google&employment_type=INTERN&hl=en_US&jlo=en_US&q=&sort_by=relevance', *args, **kwargs)
    def get_jobs(self):
        return self.bs.findAll('a')



print(Hook_Google().get_jobs())