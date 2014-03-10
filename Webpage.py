__author__ = 'ankit'

from requests import get
from redis import Redis
from BeautifulSoup import BeautifulSoup
from sets import Set

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

        tags = Set()

        for tag in parsed_html.findAll(True):
            tags.add(tag.name)

        str = ""

        tags = sorted(tags)

        for tag in tags:
            str += tag + "\n"

        return str

    def get_star(self, table_name):
        parsed_html = BeautifulSoup(redis.hget(self.url, "raw"))
        for tag in parsed_html.findAll(table_name):
            print tag