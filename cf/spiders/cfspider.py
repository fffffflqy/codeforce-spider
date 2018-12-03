import re
import sys
from cf.items import SelfItem,FriendsItem
import scrapy as scrapy
from scrapy import Selector
from scrapy.crawler import CrawlerProcess
from scrapy.http import Request, FormRequest
from scrapy.utils.project import get_project_settings



class Cfspider(scrapy.Spider):
    name = 'cf'
    id = 'huas_lqy'
    password = 'liuqiyu001'
    def start_requests(self):
        return [Request(
            'https://codeforces.com/enter?back=%2F',
            callback=self.strat_login,
            meta={'cookiejar': 1},
        )]
    def strat_login(self, response):
        self.csrf = Selector(response).xpath('//input[@name="csrf_token"]/@value').extract_first()
        return [FormRequest(
            url='https://codeforces.com/enter?back=%2F',
            method='POST',
            meta={'cookiejar':response.meta['cookiejar']},
            formdata={
                'csrf_token': self.csrf,
                'action': 'enter',
                'ftaa': '997gbl16b2vj4rurmx',
                'bfaa': '3d06cdba2d4ac5e0e98790e32b1ffa0f',
                'handleOrEmail': self.id,
                'password': self.password,
                '_tta': '155',
            },
            callback=self.after_login
        )]
    def after_login(self, response):
        if response.url == 'https://codeforces.com/':
            print('登入成功')
            self.logger.info(str(response.meta['cookiejar']))
            return [Request(
                url='https://codeforces.com/profile/'+self.id,
                meta={'cookiejar':response.meta['cookiejar']},
                callback=self.paser
            )]
        else:
            self.logger.error('登录失败')
    def paser(self, response):
        user_id = response.xpath('//div[@class="main-info "]/h1/a/text()').extract_first()
        user_rating = response.xpath('//div[@class="info"]/ul/li[1]/span/text()').extract_first()
        user_max_rating = response.xpath('//span[@class="smaller"]/span[2]/text()').extract_first()
        user_Contribution = response.xpath('//div[@class="info"]/ul/li[2]/span/text()').extract_first()
        user_friends = response.xpath('//div[@class="info"]/ul/li[3]').extract_first()
        user_mail = response.xpath('//div[@class="info"]/ul/li[6]').extract_first()
        image_urls = response.xpath('//div[@class="title-photo"]/div/div/div/img/@src').extract_first()
        image_urls='https:'+image_urls
        re_fri = re.compile(r'\d+')
        re_ma = re.compile(r"\w+([.+-]\w+)*@\w+([.-]\w+)*\.\w+([.-]\w+)*")
        user_friends = re_fri.findall(user_friends)[-1]
        user_mail = re_ma.findall(user_mail)[0]
        item = SelfItem(user_id=user_id, user_rating=user_rating, user_max_rating=user_max_rating, user_Contribution=user_Contribution, user_friends=user_friends, user_mail=user_mail, image_urls=image_urls)
        yield item
        yield Request(
            'https://codeforces.com/friends',
            meta={'cookiejar':response.meta['cookiejar']},
            callback=self.friends_paser
        )
    def friends_paser(self, response):
        # print(response.xpath('//table[@class=""]/tbody').extract_first())
        for paper in response.xpath('//table[@class=""]/tbody/tr').extract():
            # print(Selector(text=paper).xpath('//a/text()').extract_first())
            yield Request(
                url='https://codeforces.com/'+Selector(text=paper).xpath('//a/@href').extract_first(),
                meta={'cookiejar':response.meta['cookiejar']},
                callback=self.firend_message,
            )
    def firend_message(self, response):
        firend_user = response.xpath('//div[@class="main-info "]/h1/a/text()').extract_first()
        firend_rating=response.xpath('//div[@class="info"]/ul/li[1]/span/text()').extract_first()
        firend_max_rating=response.xpath('//span[@class="smaller"]/span[2]/text()').extract_first()
        if firend_max_rating == None:
            firend_max_rating = '0'
        firend_Contribution=response.xpath('//div[@class="info"]/ul/li[2]/span/text()').extract_first()
        firend_firends=response.xpath('//div[@class="info"]/ul/li[3]').extract_first()
        image_urls = response.xpath('//div[@class="title-photo"]/div/div/div/img/@src').extract_first()
        image_urls='https:'+image_urls
        # print(image_urls)
        re_fir=re.compile(r'\d+')
        firend_firends=re_fir.findall(firend_firends)[-1]
        # print(firend_user, firend_rating, firend_max_rating, firend_Contribution, firend_firends)
        item=FriendsItem(firend_user=firend_user, firend_rating=firend_rating, firend_max_rating=firend_max_rating, firend_Contribution=firend_Contribution, firend_firends=firend_firends, image_urls=image_urls)
        yield item
if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl('cf')
    process.start()