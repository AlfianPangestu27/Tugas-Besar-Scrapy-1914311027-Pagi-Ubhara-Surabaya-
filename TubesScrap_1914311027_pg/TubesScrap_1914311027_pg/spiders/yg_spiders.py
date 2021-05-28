import scrapy


class QuotesSpider(scrapy.Spider):
    name = "yg"

    def start_requests(self):
        urls = [
            'https://www.worldnovel.online/novel/i-might-be-a-fake-cultivator/',
	    'https://www.worldnovel.online/novel/forty-millenniums-of-cultivation/',
	    'https://www.worldnovel.online/novel/worlds-apocalypse-online/',
	    'https://www.worldnovel.online/novel/i-have-a-mansion-in-the-post-apocalyptic-world/',
	    'https://www.worldnovel.online/novel/gourmet-of-another-world/',
            ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')