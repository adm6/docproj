from django.test import TestCase
from .models import Article, Marathon, Reception, Consultation, Pedometer
import datetime
from django.utils import timezone
from django.test import Client


# Create your tests here.
class ArticleModel(TestCase):
    def test_article_created_success(self):
        Article.objects.create(title='test article', author='test author', content='test content',
                               created_at=datetime.datetime.now(tz=timezone.utc))
        article = Article.objects.get(title='test article')
        self.assertEqual(article.title, 'test article')
        self.assertEqual(article.author, 'test author')
        self.assertEqual(article.content, 'test content')


class ReceptionModel(TestCase):
    def test_reception_created_success(self):
        Reception.objects.create(title='test title', content='test content')
        article = Reception.objects.get(title='test title')
        self.assertEqual(article.title, 'test title')
        self.assertEqual(article.content, 'test content')


class PedometerModel(TestCase):
    def test_pedometer_created_success(self):
        Pedometer.objects.create(title='test title', content='test content')
        pedometer = Pedometer.objects.get(title='test title')
        self.assertEqual(pedometer.title, 'test title')
        self.assertEqual(pedometer.content, 'test content')


class ConsultationModel(TestCase):
    def test_reception_created_success(self):
        Consultation.objects.create(title='test title', content='test content')
        consultation = Consultation.objects.get(title='test title')
        self.assertEqual(consultation.title, 'test title')
        self.assertEqual(consultation.content, 'test content')


class MarathonModel(TestCase):
    def test_article_created_success(self):
        Marathon.objects.create(title='test title', information='test information',
                                starting_day=(timezone.now() + datetime.timedelta(days=30)),
                                ending_day=(timezone.now() + datetime.timedelta(days=75)),
                                created_at=datetime.datetime.now(tz=timezone.utc))
        Marathon.objects.create(title='test1 title', information='test1 information',
                                starting_day=(timezone.now() + datetime.timedelta(days=-75)),
                                ending_day=(timezone.now() + datetime.timedelta(days=-30)),
                                created_at=datetime.datetime.now(tz=timezone.utc))
        Marathon.objects.create(title='test2 title', information='test1 information',
                                starting_day=(timezone.now() + datetime.timedelta(days=-75)),
                                ending_day=(timezone.now() + datetime.timedelta(days=-30)),
                                created_at=datetime.datetime.now(tz=timezone.utc),
                                results='Juda zor boldi bu marafon, rahmat kotta.')
        article = Marathon.objects.get(title='test title')
        self.assertEqual(article.until_start, 30)
        self.assertEqual(article.title, 'test title')
        self.assertEqual(article.information, 'test information')
        self.assertGreater(article.ending_day, article.starting_day)
        self.assertGreater(article.until_end, article.until_start)
        article = Marathon.objects.get(title='test1 title')
        self.assertEqual(article.title, 'test1 title')
        self.assertEqual(article.information, 'test1 information')
        self.assertGreater(article.ending_day, article.starting_day)
        self.assertGreater(article.until_end, article.until_start)
        article = Marathon.objects.get(title='test2 title')
        self.assertEqual(article.results, 'Juda zor boldi bu marafon, rahmat kotta.')
        self.assertGreater(article.ending_day, article.starting_day)
        self.assertGreater(article.until_end, article.until_start)


class PagesTest(TestCase):
    def test_index_page(self):
        Article.objects.create(title='test article', author='test author', content='test content',
                               created_at=datetime.datetime.now(tz=timezone.utc))
        Article.objects.create(title='test1 article', author='test1 author', content='test1 content',
                               created_at=datetime.datetime.now(tz=timezone.utc))
        Article.objects.create(title='test2 article', author='test2 author', content='test2 content',
                               created_at=datetime.datetime.now(tz=timezone.utc))
        Article.objects.create(title='test3 article', author='test3 author', content='test3 content',
                               created_at=datetime.datetime.now(tz=timezone.utc))
        Article.objects.create(title='test4 article', author='test4 author', content='test4 content',
                               created_at=datetime.datetime.now(tz=timezone.utc))
        c = Client()
        response = c.get('/doctor/')
        self.assertEqual(response.status_code, 200)

    def test_article_page(self):
        Article.objects.create(title='test article', author='test author', content='test content',
                               created_at=datetime.datetime.now(tz=timezone.utc))
        Article.objects.create(title='test1 article', author='test1 author', content='test1 content',
                               created_at=datetime.datetime.now(tz=timezone.utc))
        Article.objects.create(title='test2 article', author='test2 author', content='test2 content',
                               created_at=datetime.datetime.now(tz=timezone.utc))
        Article.objects.create(title='test3 article', author='test3 author', content='test3 content',
                               created_at=datetime.datetime.now(tz=timezone.utc))
        Article.objects.create(title='test4 article', author='test4 author', content='test4 content',
                               created_at=datetime.datetime.now(tz=timezone.utc))
        c = Client()
        articles = Article.objects.all()
        for i in articles:
            response = c.get(f'/doctor/article/{i.pk}')
            self.assertEqual(response.status_code, 200)

    def test_marathons_page(self):
        Marathon.objects.create(title='test1 title', information='test1 information',
                                starting_day=(timezone.now() + datetime.timedelta(days=-75)),
                                ending_day=(timezone.now() + datetime.timedelta(days=-30)),
                                created_at=datetime.datetime.now(tz=timezone.utc),
                                results='Juda zor boldi bu marafon, rahmat kotta.')
        marathon = Marathon.objects.get(title='test1 title')
        c = Client()
        response = c.get(f'/doctor/marathon/{marathon.pk}')
        self.assertEqual(response.status_code, 200)

    def test_reception_page(self):
        Reception.objects.create(title='test1 title', content='test1 content')
        reception = Reception.objects.get(title='test1 title')
        c = Client()
        response = c.get(f'/doctor/reception/')
        self.assertEqual(response.status_code, 200)

    def test_pedometer_page(self):
        Pedometer.objects.create(title='test1 title', content='test1 content')
        c = Client()
        response = c.get(f'/doctor/pedometer/')
        self.assertEqual(response.status_code, 200)

    def test_consultation_page(self):
        Consultation.objects.create(title='test1 title', content='test1 content')
        consultation = Consultation.objects.get(title='test1 title')
        c = Client()
        response = c.get(f'/doctor/consultation/')
        self.assertEqual(response.status_code, 200)

    def test_articles_page(self):
        Article.objects.create(title='test article', author='test author', content='test content',
                               created_at=datetime.datetime.now(tz=timezone.utc))
        Article.objects.create(title='test1 article', author='test1 author', content='test1 content',
                               created_at=datetime.datetime.now(tz=timezone.utc))
        Article.objects.create(title='test2 article', author='test2 author', content='test2 content',
                               created_at=datetime.datetime.now(tz=timezone.utc))
        c = Client()
        response = c.get(f'/doctor/articles/')
        self.assertEqual(response.status_code, 200)
