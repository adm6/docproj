from django.test import TestCase
from .models import Article
from datetime import datetime
from django.utils import timezone
from django.test import Client


# Create your tests here.
class ArticleText(TestCase):
    def test_article_created_success(self):
        Article.objects.create(title='test article', author='test author', content='test content',
                               created_at=datetime.now(tz=timezone.utc))
        article = Article.objects.get(title='test article')
        self.assertEqual(article.title, 'test article')
        self.assertEqual(article.author, 'test author')
        self.assertEqual(article.content, 'test content')


class PagesTest(TestCase):
    def test_index_page(self):
        Article.objects.create(title='test article', author='test author', content='test content',
                               created_at=datetime.now(tz=timezone.utc))
        Article.objects.create(title='test1 article', author='test1 author', content='test1 content',
                               created_at=datetime.now(tz=timezone.utc))
        Article.objects.create(title='test2 article', author='test2 author', content='test2 content',
                               created_at=datetime.now(tz=timezone.utc))
        Article.objects.create(title='test3 article', author='test3 author', content='test3 content',
                               created_at=datetime.now(tz=timezone.utc))
        Article.objects.create(title='test4 article', author='test4 author', content='test4 content',
                               created_at=datetime.now(tz=timezone.utc))
        c = Client()
        response = c.get('/doctor/')
        self.assertEqual(response.status_code, 200)

    def test_article_page(self):
        Article.objects.create(title='test article', author='test author', content='test content',
                               created_at=datetime.now(tz=timezone.utc))
        Article.objects.create(title='test1 article', author='test1 author', content='test1 content',
                               created_at=datetime.now(tz=timezone.utc))
        Article.objects.create(title='test2 article', author='test2 author', content='test2 content',
                               created_at=datetime.now(tz=timezone.utc))
        Article.objects.create(title='test3 article', author='test3 author', content='test3 content',
                               created_at=datetime.now(tz=timezone.utc))
        Article.objects.create(title='test4 article', author='test4 author', content='test4 content',
                               created_at=datetime.now(tz=timezone.utc))
        c = Client()
        articles = Article.objects.all()
        for i in articles:
            response = c.get(f'/doctor/article/{i.pk}')
            self.assertEqual(response.status_code, 200)
