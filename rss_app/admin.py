from django.contrib import admin

from rss_app.models import News, Comment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
