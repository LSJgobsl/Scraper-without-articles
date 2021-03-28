import url_crawler
from bs4 import BeautifulSoup
import requests

def find_days(year, month):
    days = 31
    if month in month_30:
        days = 30
    elif month in month_28:
        days = 28
        if year%4 == 0:
            days = 29
    return days

class htmlparser: #blocked by recapcha
    def __init__(self):
        self.url = ""

    def get_url(self, str):
        self.url = str

    def Do_Parse(self):
        self.r = requests.get(self.url, auth=('user','pass'))
        self.html = self.r.text
        self.soup = BeautifulSoup(self.html,'html.parser')
        self.tag = self.soup.select('div.caas-body > p')

        for items in self.tag:
            print(items.text)
        


def main_scrape():
    for year in years:
        if year == 2016:# 7일 단위로
            print("scraping 2016-03-01~2016-12-31")
            for month in range(10,13):
                days = find_days(year, month)
                url_scrape.change_duration('2016-{0}-{1}'.format(month, 1), '2016-{0}-{1}'.format(month,days))
                url_scrape.get_url_list()
        elif year in range(2017,2021):
            print("scraping {0}-01-01~{0}-12-31".format(year))
            months = [1,2]
            if year == 2020:
                months = [1,2,7,8,9,10,11,12]
            for month in months:
                days = find_days(year,month)
                url_scrape.change_duration('{0}-{1}-1'.format(year, month), '{0}-{1}-{2}'.format(year, month, days))
                url_scrape.get_url_list()
        else:
            print("scraping 2021-01-01~2021-02-28")
            for month in range(1, 3):
                days = find_days(year, month)
                url_scrape.change_duration('{0}-{1}-1'.format(year, month), '{0}-{1}-{2}'.format(year,month, days))
                url_scrape.get_url_list()


if __name__ == "__main__":
    url_scrape = url_crawler.url_scraper()
    url_scrape.get_url_list()

    a = input("Do Scrape? (Y/N)\n")
    #2016-03-01 ~ 2021-02-26
    years = [2017, 2018, 2019, 2020, 2021]
    month_30 = [4,6,9,11] #30일 짜리
    month_28 = [2]#28 (단, 2016, 2020 년에는 29일)
    if (a == 'Y') or (a == 'y'):
        main_scrape()



    #test html parser
    parsing = htmlparser()
    parsing.get_url("https://finance.yahoo.com/news/sp-500-fall-15-percent-capital-economics-195838619.html")
    parsing.Do_Parse()