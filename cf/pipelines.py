# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

from cf.items import SelfItem


class CfPipeline(object):
    def __init__(self):
        self.file1 = open('self.json', 'wb')
        self.file2 = open('firends.json', 'wb')
    def process_item(self, item, spider):
        if isinstance(item, SelfItem):
            line = json.dumps(dict(item))+'\n'
            self.file1.write(line.encode('utf-8'))
        else:
            line = json.dumps(dict(item))+'\n'
            self.file2.write(line.encode('utf-8'))
        return item
class imagePipelines(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['image_urls'])

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        # item['image_paths'] = image_paths
        return item

