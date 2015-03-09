from newspaper import Article as NewsPaperArticle


class Article(NewsPaperArticle):
    def __init__(self, html, **kwargs):
        # Dummy this url as we already have the html
        # and we jsut want its parsing capabilities
        kwargs['url'] = 'http://staging.manualone.com'
        super(Article, self).__init__(**kwargs)
        # now set the html with the data we ahve
        self.set_html(html)
        # set lookup props required to make it work
        self.is_downloaded = True
