# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

import pymysql.cursors


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


class MysqlPipeline(object):
    def open_spider(self, spider):
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='linux',
                                          db='kadirTugcu',
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor,
                                          unix_socket="/opt/lampp/var/mysql/mysql.sock")

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        with self.connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `articles` (`question`, `answer`, `url`) VALUES (%s, %s, %s)"
            cursor.execute(sql, (item['question'], item['answer'], item['url']))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        self.connection.commit()
        return item
