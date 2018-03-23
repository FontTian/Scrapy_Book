# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request,FormRequest

class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['example.webscraping.com']
    start_urls = ['http://example.webscraping.com/places/default/user/profile?_next=/places/default/index']

    def parse(self, response):
        # 解析登录后的下载的界面,此处位用户个人信息页面
        keys = response.css('table label::text').re('(.+):')

        values = response.css('table td.w2p_fw::text').extract()

        yield dict(zip(keys,values))


    login_url = 'http://example.webscraping.com/places/default/user/login?_next=/places/default/index'


    def start_requests(self):
        yield Request(self.login_url,callback=self.login)


    def login(self,response):
        # 构造登录界面解析函数,构造FormRequest对象提交表单
        fd = {'email': 'fonttian@gmail.com', 'password': '123456'}

        yield FormRequest.from_response(response,formdata=fd,callback = self.parse_login)

    def parse_login(self,response):
        if 'Welcome font' in response.text:
            yield from super().start_requests()
