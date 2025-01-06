from django.urls import path

from . import views

app_name = 'article'

urlpatterns = [
    path("", views.ArticleView.as_view({'get': 'list'}), name="list"),
    path("<int:pk>", views.ArticleView.as_view({'get': 'retrieve'}), name="detail"),
]
