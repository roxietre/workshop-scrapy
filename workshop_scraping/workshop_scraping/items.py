# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from pydoc import describe
import scrapy


class WorkshopScrapingItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    describe = scrapy.Field()
    href = scrapy.Field()
    image = scrapy.Field()
    stars = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)
    pass

