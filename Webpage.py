__author__ = 'ankit'

from requests import get
from redis import Redis
from BeautifulSoup import BeautifulSoup
redis = Redis()

class Webpage(object):
    def __init__(self, url):
        self.url = url

    def get_content(self):
        r = get(self.url)
        return r.text

    def store_content(self, contents):
        redis.hset(self.url, "raw", contents)
        return contents

    def retreive_content(self):
        parsed_html = BeautifulSoup(redis.hget(self.url, "raw"))
        return parsed_html.findAll('a')[0].get('href')