from interface import *


class Hook_Waymo(Hook):
    def __init__(self, *args, **kwargs):
        super().__init__(url='https://waymo.com/joinus/', *args, **kwargs)

    def get_jobs(self):
        return self.bs.findAll('div', attrs={'class': 'careers__roles__roles'})

    def get_titles(self):
        return [job.find('div', attrs={'class': 'careers__roles__roles__role__title__role'}).getText().strip() for job in self.get_jobs()]

    def parse_jobs(self):
        jobs_dict = [{
            'title': job.find('div', attrs={'class': 'careers__roles__roles__role__title__role'}).getText().strip(),
            'link': 'https://waymo.com/joinus/' + job.find('a', {'class': 'ak-update-params'}).get('href'),
            'location': job.find('div', {'class': 'careers__roles__roles__role__title__location'}).getText().strip()
        } for job in self.get_jobs()]
        return jobs_dict


pprint(Hook_Waymo().parse_jobs())
