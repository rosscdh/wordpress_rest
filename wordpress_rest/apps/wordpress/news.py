from newspaper import Article as NewsPaperArticle


class Article(NewsPaperArticle):
    def __init__(self, html, **kwargs):
      kwargs['url'] = 'http://staging.manualone.com'
      super(Article, self).__init__(**kwargs)
      self.set_html(html)
      self.is_downloaded = True

    def build(self):
        """Build a lone article from a URL independent of the source (newspaper).
        Don't normally call this method b/c it's good to multithread articles
        on a source (newspaper) level.
        """
        self.parse()
        self.nlp()

    def download(self, html=None):
        self.set_html(html)
