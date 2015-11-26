import scrapy
from scrapy.spiders     import Spider
from scrapy.selector     import HtmlXPathSelector
from scrapy.http    import Request
from bot.vieclam24items import Vieclam24hTuyenGapItem
from bot.vieclam24items import Vieclam24hHapDanItem
from bot.vieclam24items import Vieclam24hMoiNhatItem
import re

class MySpider(Spider):
	name = "jobbot"
    	allowed_domains = ["vieclam24h.vn"]
    	start_urls = [
        	"https://vieclam24h.vn/nhan-vien-kinh-doanh-c96.html",
    	]

	def parse(self,response):
		for a in response.css("div.list-items.nganhnghe_item_right.ml_8 > div.news-title > a"):
            url = a.xpath('@href').extract()
            text = a.xpath('text()').extract()
			link = ''.join(url)
            request = scrapy.Request(link,callback=self.parse_dir_contents,meta={'dont_merge_cookies': True})
			request.meta['category'] = text
            yield request

    	def parse_dir_contents(self,response):
            category = response.meta['category']
        	for sel in response.xpath('//div[@id="nganh_tuyengap_content"]/div/div/div[contains(@class,"item_link")]'):
    			
			item = Vieclam24hTuyenGapItem()
                item["category"] = category
    			item["title"] = sel.xpath('span[contains(@class,"title-blockjob-main")]/a/text()').extract()
    			link = sel.xpath('span[contains(@class,"title-blockjob-main")]/a/@href').extract()
    			item["link"] = link
            		detail_url = ''.join(link)
            		
            		request = scrapy.Request(detail_url,callback=self.parse_detail_contents,meta={'dont_merge_cookies': True})
            		request.meta['item'] = item
            		yield request

        	for sel in response.xpath('//div[@id="nganh_hapdan_content"]/div/div/div[contains(@class,"item_link")]'):
            		item = Vieclam24hHapDanItem()
            		item["category"] = category
                    item["title"] = sel.xpath('span[contains(@class,"title-blockjob-main")]/a/text()').extract()
            		link = sel.xpath('span[contains(@class,"title-blockjob-main")]/a/@href').extract()
            		item["link"] = link
            		detail_url = ''.join(link)
            		
            		request = scrapy.Request(detail_url,callback=self.parse_detail_contents,meta={'dont_merge_cookies': True})
            		request.meta['item'] = item
            		yield request

        	for sel in response.xpath('//div[@id="nganh_vlmoi_content"]/div/div[contains(@class,"item-vlmn")]/div/div[contains(@class,"media-body")]'):
            		item = Vieclam24hMoiNhatItem() 
            		item["category"] = category
                    item["title"] = sel.xpath('div[contains(@class,"media-heading")]/a/text()').extract()
            		link = sel.xpath('div[contains(@class,"media-heading")]/a/@href').extract()
            		item["link"] = link
  			detail_url = ''.join(link)
            		
            		request = scrapy.Request(detail_url,callback=self.parse_detail_contents,meta={'dont_merge_cookies': True})
            		request.meta['item'] = item
            		yield request  

    	def parse_detail_contents(self,response):
        	item = response.meta['item']
        	boxJobDetail = response.xpath('//div[contains(@class,"box_chi_tiet_cong_viec")]')
		
        	item["company_name"] = boxJobDetail.xpath('(div[contains(@class,"row")])[1]/div/p/a/text()').extract()
        	item["company_link"] = boxJobDetail.xpath('(div[contains(@class,"row")])[1]/div/p/a/@href').extract()
        	#item["company_logo"] = response.xpath('//div[contains(@class,"logo-company")][1]/img/@src').extract()
        	rowJobDetail = boxJobDetail.xpath('div[contains(@class,"job_detail")]')
        	item["salary"] = rowJobDetail.xpath('(div[contains(@class,"col-xs-6")])[1]/p[1]/span/span[contains(@class,"job_value")]/text()').extract()
        	item["location"] = rowJobDetail.xpath('(div[contains(@class,"col-xs-6")])[2]/p[1]/span/a/text()').extract()
        	item["deadline"] = response.xpath('(//div[@id="ttd_detail"]/div[contains(@class,"job_description")]/div[2]/div[contains(@class,"item row")])[last()]/p//span[contains(@class,"text_pink")]/text()').extract()
        	hxs = HtmlXPathSelector(response)
        	item['detail'] = hxs.select('//div[@id="ttd_detail"]/*').extract()
            item['short_description'] = hxs.select('(//div[contains(@class,"row job_detail")])[1]')
		company_link = ''.join(item["company_link"])
		request = scrapy.Request(company_link,callback=self.parse_company_link,meta={'dont_merge_cookies': True})
                request.meta['item'] = item

        	yield request
	
	def parse_company_link(self,response):
		item = response.meta['item']
		item["company_logo"] = response.xpath('//div[contains(@class,"logo-company")][1]/img/@src').extract()
		yield item
		
        

            


