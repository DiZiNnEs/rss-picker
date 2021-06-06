from django.test import TestCase
from django.urls import reverse


class NewsViewTestCase(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class NewsDetailViewTestCase(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('detail/chto-takoe-python/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('detail-news'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news_detail.html')
