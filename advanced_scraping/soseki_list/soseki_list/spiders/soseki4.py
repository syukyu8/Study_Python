import scrapy, pprint


class Soseki4Spider(scrapy.Spider):
    name = 'soseki4'
    allowed_domains = ['www.aozora.gr.jp']
    #夏目漱石の作品一覧ページ
    start_urls = ['http://www.aozora.gr.jp/index_pages/person148.html']

    #作品一覧ページの解析
    def parse(self, response):
        li_list = response.css('ol > li a')
        for a in li_list:
            href = a.css('::attr(href)').extract_first()
            href2 = response.urljoin(href)
            #図書カードページの取得
            yield response.follow(
                href2, self.parse_card
            )

    #図書カードページの解析
    def parse_card(self, response):
        #タイトルの取得
        title = response.css('title::text').extract_first()
        #ダウンロード先ZIPファイルの取得
        alist = response.css('table.download tr td a')
        for a in alist:
            href = a.css('::attr(href)').extract_first()
            href2 = response.urljoin(href)
            #ZIPファイル以外は除外
            if href2[-4:] != ".zip": continue
            #ファイルをダウンロードするためにscrapy.Requestを使う
            #第一引数にはURLを、第二引数にはダウンロードが完了した時の処理を記述する
            req = scrapy.Request(
                href2, callback=self.parse_item
            )
            #メタデータにタイトルを指定する
            req.meta["title"] = title
            yield req


    #ZIPファイルの保存
    def parse_item(self, response):
        #メタデータよりファイル名を指定する
        title = response.meta["title"]
        title = title.replace('図書カード:', '').strip()
        fname = title + '.zip'
        #ファイル保存
        with open (fname, "wb") as f:
            f.write(response.body)

