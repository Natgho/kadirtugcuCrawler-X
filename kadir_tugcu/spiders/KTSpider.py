import scrapy
from w3lib.html import remove_tags

class KTSpider(scrapy.Spider):
    name = "KadirTugcuScraper"

    def start_requests(self):
        urls = [
            # firstly crawl archive... 'http://www.anneoluncaanladim.com/forum/forum_topics.asp?FID=62',
            # 'http://www.anneoluncaanladim.com/forum/forum_topics.asp?FID=218&title=cocuk-sag-ve-hastaliklari-uzm-dr-kadir-tugcu-arsivi',
            "http://www.anneoluncaanladim.com/forum/forum_posts.asp?TID=52279&title=zika-virusu",
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        question = response.xpath("//tr[@class='msgEvenTableRow'][1]/td[@class='msgLineDevider']/div[@class='msgBody']/text()").extract()
        answer = response.xpath("//tr[@class='msgOddTableRow'][1]/td[@class='msgLineDevider']/div[@class='msgBody']").extract()
        question, answer = remove_tags(question[0]).strip(), remove_tags(answer[0]).strip()
        print(question, answer)

# answer : //tr[@class='msgEvenTableRow'][1]/td[@class='msgLineDevider']/div[@class='msgBody']/text()
# question: //tr[@class='msgOddTableRow'][1]/td[@class='msgLineDevider']/div[@class='msgBody']/text()

