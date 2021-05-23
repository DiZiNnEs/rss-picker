from django.contrib.syndication.views import Feed
from django.urls import reverse

from rss_app.models import News


class LatestNewsFeed(Feed):
    title = "Police beat site news"
    link = "/sitenews/"
    description = "Updates on changes and additions to police beat central."

    def items(self):
        return News.objects.order_by('-data_published')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    def item_link(self, item):
        return reverse('news', args=[item.pk])
