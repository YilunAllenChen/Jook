from interface import *

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




pprint(Hook_Google_X().parse_jobs())