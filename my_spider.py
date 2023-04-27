import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import csv


class MySpiderSpider(CrawlSpider):
    
    def __init__(self, *args, **kwargs):
        super(MySpiderSpider, self).__init__(*args, **kwargs)

        # Open the output file and create a CSV writer object
        self.output_file = open("output.csv", "w", newline="")
        self.csv_writer = csv.writer(self.output_file)

        # Write the header row to the output file
        self.csv_writer.writerow(["link"])


    name = "my_spider"
    allowed_domains = ["itu.edu.pk"]
    start_urls = ["http://itu.edu.pk/"]
    visited_links = set()

    rules = (Rule(LinkExtractor(), callback="parse_item", follow=True),)

    def parse_item(self, response):
        for link in response.css('a::attr(href)').getall():
            if link not in self.visited_links:
                self.visited_links.add(link)
                self.csv_writer.writerow([link])
                yield scrapy.Request(link, callback=self.parse_item)

                # item = {}
                # item["link"] = link
                # yield item

    def closed(self, reason):
        self.output_file.close()