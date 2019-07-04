import rope
from scrapy.http.request import Request
import scrapy
from urllib import request
# from lxml import etree
import re
from gushici_pro.items import GushiciProItem 

class GushiciSpider(scrapy.Spider):
    name='Gushici'
    allowed_domains=['gushiwen.org']
    start_urls='https://www.gushiwen.org/default.aspx?page=1'
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/              72.0.3626.121 Safari/537.36",
            }

    def start_requests(self):
        return [scrapy.Request(self.start_urls,headers=self.headers,callback=self.parse,dont_filter=True)]

    def parse(self,response):
        text=response.text
        gushicis=re.findall(r'<div\sclass="sons">(.*?)<div\sclass="tool">',text,re.DOTALL)
        # print(gushici[0])
        # print(type(gushici))
        # print(len(gushici))
        for gushici in gushicis:
            title=re.findall(r'div\sclass="cont".*?<b>(.*?)</b>',gushici,re.DOTALL)
            print(title[0])
            dynasty=re.findall(r'div\sclass="cont".*?<p\sclass="source"><a.*?>(.*?)</a>',gushici,re.DOTALL)
            print(dynasty[0])
            author=re.findall(r'div\sclass="cont".*?<p\sclass="source"><a.*?>.*?</a>.*?<a\s.*?>(.*?)</a>',gushici,re.DOTALL)
            print(author[0])
            contents=re.findall(r'div\sclass="cont".*?<div\sclass="contson".*?>(.*?)</div>',gushici,re.DOTALL)
            content=contents[0].strip()
            print(content)
            item=GushiciProItem(title=title[0],dynasty=dynasty[0],author=author[0],content=content)
            yield item


    # def main():
        base_url='https://www.gushiwen.org/default.aspx?page={}'
        for i in range(1,10):
            yield scrapy.Request(base_url.format(i),headers=self.headers,callback=self.parse,dont_filter=False)

# if __name__=='__main__':
#     main()
    


        # poems=[]
        # poemts=[]
        # for content in contents:
        #     x=re.sub(r"<.*?>",'',content,)
        #     poems.append(x.strip())	
            
        # for value in zip(titles,dynastys,authors,poems):
        #     title,dynasty,author,poem=value
        #     content={
        #             'title':title,
        #             'dynasty':dynasty,
        #             'author':author,
        #             'poem':poem
        #             }
        #     poemts.append(content)
        
        # for poemt in poemts:
        #     print(poemt)
        #     print('=='*40)
        # return poemts	
       