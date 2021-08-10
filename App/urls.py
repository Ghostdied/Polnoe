

from App.views import mainpage, contacts, news, events, post_list, post_list_events
from django.urls import path

urlpatterns = [
    path('',mainpage),
    path('main',mainpage),
    path('contacts',contacts),
    path('news',post_list),
    path('events',post_list_events),
]
