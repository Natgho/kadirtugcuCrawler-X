import scrapy
from w3lib.html import remove_tags

from kadir_tugcu.items import KadirTugcuItem


class KTSpider(scrapy.Spider):
    name = "KadirTugcuScraper"
    base_url = "http://www.anneoluncaanladim.com/forum/"
    start_urls = ["http://www.anneoluncaanladim.com/forum/forum_topics.asp?FID=218"]

    def parse(self, response):
        for category_links in response.xpath("//tr[@class='evenTableRow']/td[2]/a/@href").extract():
            yield scrapy.Request(self.base_url + category_links, callback=self.parse_categories)

        for category_links in response.xpath("//tr[@class='oddTableRow']/td[2]/a/@href").extract():
            yield scrapy.Request(self.base_url + category_links, callback=self.parse_categories)

    def parse_categories(self, response):
        for article_link in response.xpath("//tr[@class='evenTableRow']/td[2]/div/a/@href").extract():
            next_page = response.xpath("//td[3]/a[@class='pageLink'][@title='Sonraki Sayfa']/@href").extract_first()
            if next_page is not None:
                yield scrapy.Request(self.base_url + next_page, callback=self.parse_categories)
            yield scrapy.Request(self.base_url + article_link, callback=self.parse_articles)
        for article_link in response.xpath("//tr[@class='oddTableRow']/td[2]/div/a/@href").extract():
            next_page = response.xpath("//td[3]/a[@class='pageLink'][@title='Sonraki Sayfa']/@href").extract_first()
            if next_page is not None:
                yield scrapy.Request(self.base_url + next_page, callback=self.parse_categories)
            yield scrapy.Request(self.base_url + article_link, callback=self.parse_articles)

    def parse_articles(self, response):
        question = response.xpath(
            "//tr[@class='msgEvenTableRow'][1]/td[@class='msgLineDevider']/div[@class='msgBody']").extract()
        answer = response.xpath(
            "//tr[@class='msgOddTableRow'][1]/td[@class='msgLineDevider']/div[@class='msgBody']").extract()
        question, answer = remove_tags(("".join(question)).strip()), remove_tags(("".join(answer)).strip())
        question, answer = " ".join(question.split()), " ".join(answer.split())
        category = response.xpath("//table[@class='tableBorder'][1]/tr/td/div[1]/a[4]/text()").extract_first()
        publish_date = response.xpath("//tr[2]/td[@class='msgEvenTableTop']/text()").extract()
        if len(publish_date) >= 1:
            publish_date = publish_date[-1].split(":", 1)[1].strip()
        item = KadirTugcuItem()
        item['question'] = question
        item['answer'] = answer
        item['url'] = response.url
        item['category'] = category
        item['publish_date'] = publish_date
        yield item

# answer : //tr[@class='msgEvenTableRow'][1]/td[@class='msgLineDevider']/div[@class='msgBody']/text()
# question: //tr[@class='msgOddTableRow'][1]/td[@class='msgLineDevider']/div[@class='msgBody']/text()
