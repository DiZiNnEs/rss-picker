from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase

from rss_app.models import News, Comment


class NewsModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='test', password='594231057Test')
        user = User.objects.get(id=1)
        News.objects.create(title='Python', date_published=datetime.today(), author=user,
                            text='text-text', slug='python')

    def test_first_name_label(self):
        news = News.objects.first()
        field_label = news._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')
