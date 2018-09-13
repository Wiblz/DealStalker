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
        self.add_field = ("INSERT INTO Products " 
              "(%s) "
              "VALUES ('%s')")
        self.update_field = ("UPDATE Products " 
              "SET %s = '%s' "
              "WHERE ModelName='%s'")
        self.update_int = ("UPDATE Products " 
              "SET %s = %s "
              "WHERE ModelName='%s'")

        self.update_gender = (""" UPDATE Products SET Gender='u' WHERE InnerId='%s' AND Color='%s' """ )

    
    def process_item(self, item, spider):

        self.duplicate_check =  """ SELECT Color, InnerId, Gender FROM Products WHERE Color='%s' AND InnerId='%s' """ % (item['color'][0], item['inner_id'][0])


        self.cursor.execute(self.duplicate_check)

        print("\n\n\n\n\n\n\n\n\n\n\n\n")
        print(self.add_field % ('ModelName',item['model'][0]))

        dupiclicates = self.cursor.fetchone()
        
        if dupiclicates is None: 
            #self.cursor.execute(self.add_product, 
            #(item['brand'][0].encode('utf-8'),
            #item['model'][0].encode('utf-8'),
            #item['description'][0].encode('utf-8'),
            #item['price'][0],
            #item['price_currency'][0].encode('utf-8'),
            #item['image'][0].encode('utf-8'), 
            #item['url'][0].encode('utf-8'), 
            #item['is_discounted'][0]),
            #item['color'][0].encode('utf-8'),
            #item['inner_id'][0].encode('utf-8'),
            #item['gender'][0].encode('utf-8'))
            if 'model' in item: 
                print(self.add_field % ('ModelName',item['model'][0]))
                self.cursor.execute(self.add_field % ('ModelName',item['model'][0]))
            if 'description' in item: 
                print(self.update_field % ('Description',item['description'][0],item['model'][0]))
                self.cursor.execute(self.update_field % ('Description',item['description'][0],item['model'][0]))
            if 'price' in item:
                print(self.update_int % ('Price',item['price'][0],item['model'][0])) 
                self.cursor.execute(self.update_int % ('Price',item['price'][0],item['model'][0]))
            if 'price_currency' in item:
                print(self.update_field % ('PriceCurrency',item['price_currency'][0],item['model'][0])) 
                self.cursor.execute(self.update_field % ('PriceCurrency',item['price_currency'][0],item['model'][0]))
            if 'image' in item: 
                print(self.update_field % ('ImageUrl',item['image'][0],item['model'][0]))
                self.cursor.execute(self.update_field % ('ImageUrl',item['image'][0],item['model'][0]))
            if 'url' in item: 
                print(self.update_field % ('SourceUrl',item['url'][0],item['model'][0]))
                self.cursor.execute(self.update_field % ('SourceUrl',item['url'][0],item['model'][0]))
            if 'is_discounted' in item: 
                self.cursor.execute(self.update_field % ('isDiscounted',item['is_discounted'][0],item['model'][0]))
            if 'color' in item: 
                self.cursor.execute(self.update_field % ('Color',item['color'][0],item['model'][0]))
            if 'inner_id' in item: 
                self.cursor.execute(self.update_field % ('InnerId',item['inner_id'][0],item['model'][0]))
            if 'gender' in item: 
                self.cursor.execute(self.update_field % ('Gender',item['gender'][0],item['model'][0]))
            if 'brand' in item: 
                self.cursor.execute(self.update_field % ('Brand',item['brand'][0],item['model'][0]))
        else:
            if item['gender'][0] != dupiclicates['Gender']:
                self.cursor.execute(self.update_gender,(item['inner_id'][0],item['color'][0]))

        
        self.cnx.commit()
        return item


    def close_spider(self, spider):
        self.cursor.close()
        self.cnx.close()


            
