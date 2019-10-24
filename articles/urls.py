from django.urls import path
from . import views 

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/detail/', views.detail, name='detail'),
    path('<int:article_pk>/update/', views.update, name='update'),
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    path('<int:article_pk>/commentcreate/', views.commentcreate, name='commentcreate'),
    path('<int:article_pk>/commentdelete/<int:comment_pk>/', views.commentdelete, name='commentdelete'),
    path('<int:article_pk>/liked/', views.liked, name='liked'),
]
