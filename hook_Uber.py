from interface import *


class Hook_Uber(Hook):
    def __init__(self, *args, **kwargs):
        filters = {
            "Advanced%20Technologies%20Group": [
                'General%20&%20Administrative',
                'Global%20Supply%20Chain%20&%20Business%20Operations',
                'Hardware%20Engineering%20&%20Vehicle%20Programs',
                'Product%20and%20Design',
                'Research%20&%20Development',
                'Software',
                'Systems%20Engineering%20&%20Testing',
                'Systems%20Safety',
                'Technical%20Program%20Management'
            ],
            "Business%20Development%20&%20Sales": ['Business', 'Business%20Development', 'Sales'],
            "Communications": ["Communications"],
            "Community%20Operations": ["Community%20Operations"],
            "Data%20Science": ["Data%20Science"],
            "Design": ["Design"],
            "Engineering": ['Android',
                            'Backend',
                            'Data',
                            'Engineering',
                            'Freight',
                            'Frontend',
                            'iOS',
                            'IT%20Eng',
                            'Machine%20Learning',
                            'Manager',
                            'Staff/TLM',
                            'Systems%20Engineering%20&%20Testing',
                            'Technical%20Program%20Manager'],
            "Finance%20&%20Accounting": ['Accounting',
                                         'Finance%20Operations',
                                         'Finance%20Technology',
                                         'Internal%20Audit',
                                         'Strategic%20Finance',
                                         'Tax'],
            "Legal": ["Legal"],
            "Marketing": ['Central%20Marketing',
                          'Local%20Marketing',
                          'Product%20Marketing%20Management'],
            "Operations%20&%20Launch": ['Central%20Operations',
                                        'City%20Operations',
                                        'Product%20Operations'],
            "People%20&%20Places": ['People',
                                    'Recruiting',
                                    'Strategy%20&%20Leadership'],
            "Product": ['Product%20Management',
                        'Program%20Management'],
            "Public%20Policy": ["Public%20Policy"],
            "Safety,Security%20&%20Insurance": ['Engineering%20Security',
                                                'Insurance',
                                                'Physical%20Security',
                                                'Trust%20&%20Safety'],
            "University": ['Business%20&%20Sales',
                           'Engineering',
                           'Marketing',
                           'Operations']
        }
        super().__init__(url='https://www.uber.com/us/en/careers/list/?', *args, **kwargs)

    def get_jobs(self):
        return self.bs.findAll('li', attrs={'class': 'job-listing js-job-listing -visible'})

    def get_titles(self):
        return [job.find('h4', attrs={'class': 'job-title'}).getText() for job in self.get_jobs()]

    def parse_jobs(self):
        jobs_dict = [{
            'title': job.find('h4', attrs={'class': 'job-title'}).getText(),
            'link': 'https://x.company/' + job.find('a', {'class': 'job-link ak-update-params'}).get('href'),
            'location': job.find('p', {'class': 'job-location'}).getText(),
            'date_updated': datetime.fromisoformat(job.get('data-updated'))
        } for job in self.get_jobs()]
        return jobs_dict


pprint(Hook_Uber().parse_jobs())
