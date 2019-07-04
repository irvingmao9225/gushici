# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import CsvItemExporter
class GushiciProPipeline(object):
    def __init__(self):
        self.fp=open("Gushici.csv",'wb')
        self.exporters=CsvItemExporter(self.fp,encoding="utf-8")
        self.exporters.fields_to_export = ["title","dynasty","author","content"]
        self.exporters.start_exporting()
    def process_item(self, item, spider):
        # item_json=json.dumps(dict(item),ensure_ascii=False)
        # self.fp.write(item_json+'/n')
        self.exporters.export_item(item)
        return item
    def close_spider(self,spider):
        self.exporters.finish_exporting()
        self.fp.close()
        print("end")
    
