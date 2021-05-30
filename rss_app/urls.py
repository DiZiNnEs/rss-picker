from django.urls import path

from rss_app.rss import LatestNewsFeed
from rss_app.views import NewsView, NewsDetail

urlpatterns = [
    path('', NewsView.as_view(), name='index'),
    path('detail/<slug>/', NewsDetail.as_view(), name='detail-news'),
    path('feed/', LatestNewsFeed()),
]
