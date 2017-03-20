from django.contrib import admin
from myblog.models import *


# from django_markdown.admin import MarkdownModelAdmin
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    fields = ('title', 'desc', 'content',)
    # list_display = ('title','desc','content',)


admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Category)
# admin.site.register(ArticleManager)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)
