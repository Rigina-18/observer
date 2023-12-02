from django.contrib import admin

from blog.models import Review, Topic, Like
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    list_display = ['id', 'topic', 'title']
    list_display_links = ['id', 'title']
    list_filter = ['topic']
    list_editable = ['topic']


admin.site.register(Topic)
admin.site.register(Like)
