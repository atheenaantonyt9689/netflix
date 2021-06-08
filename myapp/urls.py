

from django.urls import path
from .views import HomePageView,FilterView
urlpatterns = [
path('', FilterView.as_view(), name='kk'),
path('filter', HomePageView.as_view(), name='home'),
]
