import scrapy

#Spiderを継承してクラスを作る
class SosekiSpider(scrapy.Spider):
    name = 'soseki2' #Spiderの名前
    start_urls = [ #取得対象のWebサイト
        'https://www.aozora.gr.jp/index_pages/person148.html'
    ]

    def parse(self, response):
        #作品一覧を抽出
        li_list = response.css('ol > li a')
        for a in li_list:
            #href属性とテキストを取り出す
            href = a.css('::attr(href)').extract_first() #最初の要素を返す
            text = a.css('::text').extract_first()

            #相対パスから絶対パスに変換
            href2 = response.urljoin(href)
            #結果を返す
            yield{
                'text': text,
                'url': href2
            }
