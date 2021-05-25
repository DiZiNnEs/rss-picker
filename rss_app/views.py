from django.views.generic import DetailView

from rss_app.models import News


class NewsDetail(DetailView):
    template_name = 'news_detail.html'
    model = News


