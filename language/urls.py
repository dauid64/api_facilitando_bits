from django.urls import path

from . import views

app_name = 'language'

urlpatterns = [
    path('', views.LanguageView.as_view({'get': 'list'}), name='list'),
    path('<str:code>', views.LanguageView.as_view({'get': 'retrieve'}), name='detail'),
]
