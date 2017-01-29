# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class JsonWriterPipeline(object):

    # def process_item(self, item, spider):
    #     print("Bu question kismi:", item['question'])
    #     print("Bu answer kismi:", item['answer'])
    #     print("Bu link kismi:", item['url'])

    def open_spider(self, spider):
        self.file = open('items.json', 'w+', encoding="utf-8")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.writelines(line)
        return item


# class KadirTugcuPipeline(object):
#
#     def process_item(self, item, spider):
#         return item
