from django.urls import path, re_path
from . import views

app_name = 'articles'

urlpatterns = [
    path('',views.article_page, name = 'list'),
    path('create/', views.article_create, name = 'create' ),
    path('<slug:slug>/', views.article_details, name ='detail')
]
