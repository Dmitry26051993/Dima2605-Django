from django.urls import path

from catdog.views import catdog_view

urlpatterns = [
    path('', catdog_view, name='catdog'),
]