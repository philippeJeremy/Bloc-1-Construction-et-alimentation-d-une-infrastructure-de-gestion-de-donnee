import os
import json
import scrapy
import logging

from scrapy.crawler import CrawlerProcess

# Information complémentaire sur les hôtels
class QuotesSpider2(scrapy.Spider):
    name = "spider2"
    file = open("hotel_1.json")
    file = json.load(file)
    liste_urls = [element["url"] for element in file] 

    start_urls = liste_urls
        
    def parse(self, response):
            
            a = response.css('#hotel_address::attr(data-atlas-latlng)').get(),
            b = a[0]
            c = b.split(",")
            
            yield {
                "hotel": response.css('h2.pp-header__title::text').get(),
                "description" : response.css('#property_description_content > p::text').get(),
                "latitutde": c[0],
                "longitude": c[1],
            }
        
filename = "hotel_2.json"

if filename in os.listdir():
        os.remove( filename)
        
process = CrawlerProcess(settings = {
    'USER_AGENT': 'Chrome/97.0',
    'LOG_LEVEL': logging.INFO,
    "FEEDS": {
        filename : {"format": "json"},
    },
    "AUTOTHROTTLE_ENABLED": True
})

process.crawl(QuotesSpider2)
process.start()