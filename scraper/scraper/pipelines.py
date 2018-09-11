# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector
import pymysql


class ScraperPipeline(object):
    def __init__(self):
        self.cnx = mysql.connector.connect(user='root', password='12345Black!',
                                 host='localhost',
                                 database='dealstalker')
        self.cursor = self.cnx.cursor()

    
    def process_item(self, item, spider):

        add_product = ("INSERT INTO Products "
              "(Brend, ModelName, Description,Price, PriceCurrency,ImageUrl, SourceUrl,isDiscounted) "
              "VALUES (%s, %s, %s, %s ,%s, %s, %s, %s)" )
        
        self.cursor.execute(add_product, 
        (item['brand'][0].encode('utf-8'),
        item['model'][0].encode('utf-8'),
        item['description'][0].encode('utf-8'),
        item['price'][0],
        item['price_currency'][0].encode('utf-8'),
        item['image'][0].encode('utf-8'), 
        item['url'][0].encode('utf-8'), 
        item['is_discounted'][0]))
        
        self.cnx.commit()

        return item


    def close_spider(self, spider):
        self.cursor.close()
        self.cnx.close()


            
