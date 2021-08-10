from django.contrib import admin
from App.models import *
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(Callback)

class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)

admin.site.register(News, NewsAdmin)

class EventsAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)

admin.site.register(Events, NewsAdmin)