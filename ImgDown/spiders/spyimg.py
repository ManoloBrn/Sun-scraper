import scrapy


class ImgSpider(scrapy.Spider):
    name = "spyimg"
    start_urls = [
        'https://benandfrank.com/collections/optico-mujer'
    ]

    def parse(self, response):
        items = response.css('.product-list-item')
        urls_img = []      
        data = []
        for item in items:
            url = 'http://'+item.css('div > figure > a > div > img::attr(src)').extract()[0][2::]
            name = item.css('div > section > a::text').extract()
            data.append({'name':name, 'url':url})
            urls_img.append(url)

        yield {
                'image_urls': urls_img,
                'data':data
            }
           