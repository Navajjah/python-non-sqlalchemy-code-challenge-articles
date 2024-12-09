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
        if not isinstance(name, str):
            raise ValueError('Magazine name has to be a string')
        if not isinstance(category, str):
            raise ValueError('Magazine category must be a string')
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            print(f"Invalid new asssignment. '{value}' is not a valid string.") 

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            print(f"Invalid new asssignment. '{value}' is not a valid string.")

    def articles(self):
        return[article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        articles = self.articles()
        if articles:
            return[article.title for article in articles]
        return None

    def contributing_authors(self):
        number_of_authors = {}
        
        for article in self.articles():
            if article.author in number_of_authors:
                number_of_authors[article.author] += 1
            else:
                number_of_authors[article.author] = 1
        contributing_authors = [author for author, number in number_of_authors.items() if number > 2]
    
        return contributing_authors if contributing_authors else None