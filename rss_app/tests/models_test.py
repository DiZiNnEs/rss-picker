import datetime

import pytz
from django.contrib.auth.models import User
from django.test import TestCase

from rss_app.models import News, Comment


class NewsModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='test', password='594231057Test')
        user = User.objects.get(id=1)
        News.objects.create(title='Python', pub_date='2021-09-19 08:47:51.807533',
                            author=user,
                            text='text-text', slug='python')

    def test_title_field(self):
        news = News.objects.first()
        field = news.title
        self.assertEqual(field, 'Python')

    def test_pub_date_field(self):
        news = News.objects.first()
        field = str(news.pub_date)
        self.assertEqual(field, '2021-09-19 08:47:51.807533+00:00')

    def test_author_field(self):
        news = News.objects.first()
        field = news.author.username
        self.assertEqual(field, 'test')

    def test_test_field(self):
        news = News.objects.first()
        field = news.text
        self.assertEqual(field, 'text-text')

    def test_slug_field(self):
        news = News.objects.first()
        field = news.slug
        self.assertEqual(field, 'python')

    def test_get_absolute_url(self):
        news = News.objects.first()
        field = news.get_absolute_url()
        self.assertEqual(field, '/detail/python/')


class CommentModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='test', password='594231057Test')
        user = User.objects.get(id=1)
        News.objects.create(title='Python', pub_date='2021-09-19 08:47:51.807533',
                            author=user,
                            text='text-text', slug='python')
        news = News.objects.get(id=1)
        Comment.objects.create(author=user, text='bla-bla-bla', news=news)

    def test_author_field(self):
        comment = Comment.objects.first()
        field = comment.author
        user = User.objects.get(id=1)
        self.assertEqual(field, user)

    def test_text_field(self):
        comment = Comment.objects.first()
        field = comment.text
        self.assertEqual(field, 'bla-bla-bla')

    def test_text_news(self):
        comment = Comment.objects.first()
        field = comment.news
        news = News.objects.first()
        self.assertEqual(field, news)
