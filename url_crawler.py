import bs4
import requests
import pandas as pd
import feedparser
from pandas import DataFrame
from time import mktime
from datetime import datetime

<<<<<<< HEAD
from numpy import random
import json
=======
>>>>>>> parent of e486b6f (csv to json)
import csv
import time

#date on parse date

<<<<<<< HEAD

class htmlparser: #blocked by recapcha
    def __init__(self):
        self.url = ""
        self.contents = ""

    def get_url(self, str):
        self.url = str

    def Do_Parse(self):
        self.contents = ""
        self.r = requests.get(self.url, auth=('user','pass'))
        a = random.randint(1,high=3)
        time.sleep(a)
        self.html = self.r.text
        self.soup = BeautifulSoup(self.html,'html.parser')
        self.tag = self.soup.select('div.caas-body > p')

        for items in self.tag:
            self.contents = self.contents +"\n"+ items.text
        return self.contents


=======
>>>>>>> parent of e486b6f (csv to json)
class url_scraper:
  def __init__(self):
    self.site = "finance.yahoo.com"
    self.url = "https://news.google.com/rss/search?q=s%26p500%20site%3A{0}&hl=en-US&gl=US&ceid=US%3Aen".format(self.site)
    self.parse_rss = feedparser.parse(self.url)
    self.parse_rss.entries[0]
    self.col = ['title', 'url', 'when']
    self.rss_key = []
    self.rss_val = []
    self.rss_date = []
    self.duration = 0
    
  def get_url_list(self):
    for p in self.parse_rss.entries:
      self.rss_key.append(p.title)
      self.rss_val.append(p.link)
      date_ = mktime(p.published_parsed)
<<<<<<< HEAD
      tmp_dict = {}
      tmp_dict['title']=p.title
      tmp_dict['link'] = p.link
      tmp_dict['content']=content
      tmp_dict['date'] = datetime.fromtimestamp(date_).strftime("%Y-%m-%d")
      self.list4json.append(tmp_dict)
      #print(self.list4json)
    with open('./scraper/{0}news.json'.format(self.duration),'w') as f:
      json.dump(self.list4json, f)
=======
      
      self.rss_date.append(datetime.fromtimestamp(date_).date())
    df = DataFrame( [self.rss_key, self.rss_val, self.rss_date], index=self.col)
    df = df.T
    df.to_csv('./scraper/url_{0}.csv'.format(self.duration))
>>>>>>> parent of e486b6f (csv to json)

  def change_duration(self, start, end):
    self.search = "google%20OR%20apple%20microsoft%20OR%20Netflix%20OR%20Amazon%20OR%20FaceBook"
    self.url = "https://news.google.com/rss/search?q={0}%20site%3A{1}%20before%3A{2}%20after%3A{3}&hl=en-US&gl=US&ceid=US%3Aen".format(self.search,self.site, end, start)
    print(self.url)
    self.parse_rss = feedparser.parse(self.url)
    self.parse_rss.entries[0]
    self.rss_key = []
    self.rss_val = []
    self.rss_date = []
    self.duration = '{0}_{1}'.format(start,end)
