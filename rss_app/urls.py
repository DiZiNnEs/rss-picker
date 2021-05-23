from django.urls import path

from rss_app.rss import LatestNewsFeed

urlpatterns = [
    path('feed/', LatestNewsFeed()),
]
