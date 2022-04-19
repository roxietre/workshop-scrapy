from unicodedata import name

from numpy import imag
from ..items import WorkshopScrapingItem
import scrapy


class EcommerceSpider(scrapy.Spider):
    name = 'ecommerce'
    allowed_domains = ['webscraper.io']
    start_urls = ['https://webscraper.io/test-sites/e-commerce/static']

    def parse(self, response):
        items = WorkshopScrapingItem()
        name_c = response.xpath('//div[contains(@class, "col-sm-4 col-lg-4 col-md-4")]//a')
        for name in name_c:
            items['name'] = name.css('::text').extract()
            yield items
        price_c = response.xpath('//div[contains(@class, "col-sm-4 col-lg-4 col-md-4")]//h4[contains(@class, "pull-right price")]')
        for price in price_c:
            items['price'] = price.css('::text').extract()
            yield items
        describe_c = response.xpath('//div[contains(@class, "col-sm-4 col-lg-4 col-md-4")]//p[contains(@class, "description")]')
        for describe in describe_c:
            items['describe'] = describe.css('::text').extract()
            yield items
        href_c = response.xpath('//div[contains(@class, "col-sm-4 col-lg-4 col-md-4")]//a/@href')
        for href in href_c:
            items['href'] = href.extract()
            yield items
        image_c = response.xpath('//div[contains(@class, "col-sm-4 col-lg-4 col-md-4")]//img/@src')
        for image in image_c:
            items['image'] = image.extract()
            yield items
        stars_c = response.xpath('//div[contains(@class, "col-sm-4 col-lg-4 col-md-4")]//div[contains(@class, "rating")]/@data-rating')
        for stars in stars_c:
            items['stars'] = stars.extract()
            yield items