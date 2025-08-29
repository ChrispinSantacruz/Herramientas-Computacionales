import scrapy


class Population2025Spider(scrapy.Spider):
    name = "population2025"
    allowed_domains = ["worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/"]

    custom_headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/127.0.0.1 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9,es;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, headers=self.custom_headers, callback=self.parse)

    def parse(self, response):
        rows = response.xpath(
            '//table[@class="table table-striped table-bordered table-hover table-condensed table-list"]/tbody/tr'
        )
        for row in rows:
            yield {
                "Country": row.xpath(".//td[2]/a/text()").get(),
                "Population": row.xpath(".//td[3]/text()").get(),
                "YearlyChange": row.xpath(".//td[4]/text()").get(),
                "NetChange": row.xpath(".//td[5]/text()").get(),
                "Density": row.xpath(".//td[6]/text()").get(),
                "LandArea": row.xpath(".//td[7]/text()").get(),
                "Migrants": row.xpath(".//td[8]/text()").get(),
                "FertilityRate": row.xpath(".//td[9]/text()").get(),
                "MedianAge": row.xpath(".//td[10]/text()").get(),
                "UrbanPop": row.xpath(".//td[11]/text()").get(),
                "WorldShare": row.xpath(".//td[12]/text()").get(),
            }
