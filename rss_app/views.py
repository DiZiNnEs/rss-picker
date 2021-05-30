from django.views import generic

from rss_app.models import News


class NewsView(generic.ListView):
    template_name = 'index.html'
    model = News
    context_object_name = 'news_list'


class NewsDetail(generic.DetailView):
    template_name = 'news_detail.html'
    model = News
