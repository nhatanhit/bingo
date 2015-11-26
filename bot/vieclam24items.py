import scrapy
from scrapy.item import Item, Field
from scrapy.spiders  import Spider


class Vieclam24hTuyenGapItem(scrapy.Item):
	status = "Tuyen Gap"
	title = scrapy.Field()
	link = scrapy.Field()
	company_link = scrapy.Field()
	company_name = scrapy.Field()
	company_logo = scrapy.Field()
	salary = scrapy.Field()
	deadline = scrapy.Field()
	location = scrapy.Field()
	detail = scrapy.Field()
	short_description = scrapy.Field()
	category = scrapy.Field()

class Vieclam24hHapDanItem(scrapy.Item):
	status = "Hap Dan"
	title = scrapy.Field()
	link = scrapy.Field()
	company_link = scrapy.Field()
	company_name = scrapy.Field()
	company_logo = scrapy.Field()
	salary = scrapy.Field()
	deadline = scrapy.Field()
	location = scrapy.Field()
	detail = scrapy.Field()
	category = scrapy.Field()
	short_description = scrapy.Field()

class Vieclam24hMoiNhatItem(scrapy.Item):
	status = "Moi Nhat"
	title = scrapy.Field()
	link = scrapy.Field()
	company_link = scrapy.Field()
	company_name = scrapy.Field()
	company_logo = scrapy.Field()
	salary = scrapy.Field()
	deadline = scrapy.Field()
	location = scrapy.Field()
	detail = scrapy.Field()
	category = scrapy.Field()
	short_description = scrapy.Field()
