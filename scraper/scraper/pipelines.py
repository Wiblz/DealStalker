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
        
        self.add_field = ("INSERT INTO Products " "(%s) " "VALUES (%s)")

        self.update_gender = (""" UPDATE Products SET Gender='u' WHERE InnerId='%s' AND Color='%s' """ )
        self.update_price = (""" UPDATE Products SET Price=%s WHERE InnerId='%s' AND Color='%s' """ )
        self.update_source = (""" UPDATE Products SET SourceUrl='%s' WHERE InnerId='%s' AND Color='%s' """ )
        self.update_discount = (""" UPDATE Products SET isDiscounted=%s WHERE InnerId='%s' AND Color='%s' """ )

    def process_item(self, item, spider):

        duplicate_check =  """ SELECT Color, InnerId, Gender, Price, SourceUrl FROM Products WHERE Color='%s' AND InnerId='%s' AND ResourceUrl='%s'""" % (item['color'][0], item['inner_id'][0],item['resource'][0])
        
        self.cursor.execute(duplicate_check)
        
        dupiclicates = self.cursor.fetchone()
        
        if dupiclicates is None: 
            field_list = []
            name_str = ''
            if 'model' in item: 
                field_list.append(item['model'][0].encode('utf8').decode())
                name_str += ' ModelName'
            if 'description' in item: 
                field_list.append(item['description'][0].encode('utf8').decode())
                name_str += ', Description'
            if 'price' in item:
                field_list.append(item['price'][0])
                name_str += ', Price'
            if 'price_currency' in item:
                field_list.append(item['price_currency'][0].encode('utf8').decode())
                name_str += ', PriceCurrency'
            if 'image' in item: 
                field_list.append(item['image'][0].encode('utf8').decode())
                name_str += ', ImageUrl'
            if 'url' in item: 
                field_list.append(item['url'][0].encode('utf8').decode())
                name_str += ', SourceUrl'
            if 'is_discounted' in item: 
                field_list.append(item['is_discounted'][0])
                name_str += ', isDiscounted'
            if 'color' in item: 
                field_list.append(item['color'][0].encode('utf8').decode())
                name_str += ', Color'
            if 'inner_id' in item: 
                field_list.append(str(item['inner_id'][0]).encode('utf8').decode())
                name_str += ', InnerId'
            if 'gender' in item: 
                field_list.append(item['gender'][0].encode('utf8').decode())
                name_str += ', Gender'
            if 'brand' in item: 
                field_list.append(item['brand'][0].encode('utf8').decode())
                name_str += ', Brand'
            if 'resource' in item: 
                field_list.append(item['resource'][0].encode('utf8').decode())
                name_str += ', ResourceUrl'
            # Create and execute query
            format_strings = ','.join(['%s'] * len(field_list))
            self.cursor.execute(self.add_field % (name_str, format_strings),
                tuple(field_list))
        else:
            if 'gender' in item and item['gender'][0] != dupiclicates[2]:
                self.cursor.execute(self.update_gender % (item['inner_id'][0],item['color'][0]))
            #Here should be mechanism for adding price to monitor struct
            if 'price' in item and item['price'][0] != dupiclicates[3]:
                self.cursor.execute(self.update_price % (item['price'][0],item['inner_id'][0],item['color'][0]))
            if item['url'][0] != dupiclicates[4]:
                self.cursor.execute(self.update_source % (item['url'][0],item['inner_id'][0],item['color'][0]))
        
        self.cnx.commit()
        return item


    def close_spider(self, spider):
        self.cursor.close()
        self.cnx.close()


            
