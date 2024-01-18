from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('add-event', add_event, name='add-event'),
    path('search/', EventSearchView.as_view(), name='event-search'),
    path('events-by-category/<int:category_id>/', events_by_category, name='show-event'),
]