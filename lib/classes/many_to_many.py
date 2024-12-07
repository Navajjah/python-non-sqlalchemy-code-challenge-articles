from typing import Any


class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        if hasattr(self, 'title'):
            raise AttributeError('title is immutable')
        self.title = title
        Article.all.append(self)
        
class Author:
    def __init__(self, name):
        self._name = name

    def __setattr__(self, name, value):
        if hasattr(self, '_name'):
            raise AttributeError('name is immutable')
        super().__setattr__(name, value)

    @property
    def name(self):
        return self._name

    def articles(self):
        return[article for article in Article.all if article.author == self]

    def magazines(self):
       return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
       return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        
        return list(set(article.magazine.category for article in self.articles()))

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        return[article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        return[article.title for article in self.articles()]

    def contributing_authors(self):
        return[article.author.name for article in self.articles()] 