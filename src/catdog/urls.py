from django.urls import path

from catdog.views import catdog_view, save_catdog, send_email, pet_filter

urlpatterns = [
    path('', catdog_view, name='catdog'),
    path('save_catdog', save_catdog, name='save_catdog'),
    path('send_mail', send_email, name='send_mail'),
    path('pet_filter', pet_filter, name='pet_filter'),
]