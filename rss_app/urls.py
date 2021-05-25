from django.urls import path

from rss_app.rss import LatestNewsFeed
from rss_app.views import NewsDetail

urlpatterns = [
    path('detail-news/<slug>/', NewsDetail.as_view(), name='detail-news'),
    path('feed/', LatestNewsFeed()),
]
