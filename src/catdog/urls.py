from django.urls import path

from catdog.views import catdog_view, save_catdog, send_email

urlpatterns = [
    path('', catdog_view, name='catdog'),
    path('save_catdog', save_catdog,
         name='save_catdog'),
    path('send_mail', send_email, name='send_mail'),
]