from cf.middlewares.resource import PROXYS
import random
class RandomProxy(object):
    def process_requset(self, request, spider):
        proxy = random.choice(PROXYS)
        request.meta['proxy'] = 'https://%s'%proxy