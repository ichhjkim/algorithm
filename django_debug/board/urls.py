from django.urls import path
from . import views

app_name='board'

urlpatterns = [
    # C 만들기, 
    path('articles/new/', views.new_article, name='new_article'),
    # R 보여주기
    path('articles/<int:article_id>/', views.article_detail, name='article_detail'),
    # U
    path('articles/<int:article_id>/update/',views.article_update, name='article_update' ),
    # D
    path('articles/<int:article_id>/delete/', views.article_delete, name='article_delete'),
    # 댓글 생성
    path('articles/<int:article_id>/comments/', views.create_comment, name='create_comment'),
    # 댓글 삭제
    path('articles/<int:article_id>/comments/<int:comment_id>/delete', views.delete_comment, name='delete_comment'),

]
