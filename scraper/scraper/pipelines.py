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

        self.add_product = ("INSERT INTO Products "
              "(Brand, ModelName, Description,Price, PriceCurrency,ImageUrl, SourceUrl,isDiscounted, Color, InnerId, Gender) "
              "VALUES (%s, %s, %s, %s ,%s, %s, %s, %s,%s, %s, %s)" )

        self.duplicate_check = ("SELECT Color, InnerId, Gender FROM customers WHERE Color='%s' AND InnerId='%s' ")
        self.update_gender = ("UPDATE Products SET Gender='u' WHERE InnerId='%s' AND Color='%s'")

    
    def process_item(self, item, spider):

        
        self.cursor.execute(self.duplicate_check,
        	item['color'][0].encode('utf-8'),
        	item['inner_id'][0].encode('utf-8'))

        dupiclicates = self.cursor.fetchall()
        
        if dupiclicates is None:
            self.cursor.execute(self.add_product, 
            (item['brand'][0].encode('utf-8'),
            item['model'][0].encode('utf-8'),
            item['description'][0].encode('utf-8'),
            item['price'][0],
            item['price_currency'][0].encode('utf-8'),
            item['image'][0].encode('utf-8'), 
            item['url'][0].encode('utf-8'), 
            item['is_discounted'][0]),
            item['color'][0].encode('utf-8'),
            item['inner_id'][0].encode('utf-8'),
            item['gender'][0].encode('utf-8'))
        else:
            if item['gender'][0].encode('utf-8') != dupiclicates[0]['Gender'].encode('utf-8'):
                self.cursor.execute(self.update_gender,item['inner_id'],item['color'])

            	
        
        self.cnx.commit()
        return item


    def close_spider(self, spider):
        self.cursor.close()
        self.cnx.close()


            
