#coding=utf-8
import scrapy
from scrapy.http import Request
from scrapy.http import FormRequest
from yanchang.items import YanchangItem
import json

class zhanhui(scrapy.Spider):
    name = "yanchang"
    allowed_domains = ["damai.cn"]
    def start_requests(self):
        link="http://search.damai.cn/searchajax.html"
        n=1
        while(n<=6):
            s=str(n);
            print type(s)
            formdata={'ctl':'体育比赛','currPage':s}
            yield FormRequest(link, callback=self.parse, formdata=formdata)
            n=n+1
    def parse(self, response):
        jsonbody=json.loads(response.body)
        jsonbody=jsonbody['pageData']['resultData']
        for i in jsonbody:
            url="http://piao.damai.cn/"
            site=str(i["projectid"])
            url=url+site+".html"
            yield Request(url,callback=self.parse_next)

    def  parse_next(self,response):
        item=YanchangItem()
        for sel in response.xpath("//div[@class='m-goods']"):
            title=sel.xpath("h2/span/text()").extract()
            for i in title:
                item['title']=i.replace(' ','')
            s=response.xpath("//table[@class='m-table2']/tbody/tr")
            time=s[0].xpath("td/text()").extract()
            item['stime']=time[1].replace(" ","")[0:10].replace("-",'')
            item['etime']=time[1].replace(" ","")[-10:].replace("-",'')
            item['address']=time[3]
            address=response.xpath("//div[@class='sd']/div/div/p/a[@target='_blank']/text()").extract()
            for i in address:
                i.replace(' ','')
                item['city']=i[-3:-1]
            item['yc1']='1'
            item['chengren']='1'
            
            print item['title'],item['stime'],item['etime']