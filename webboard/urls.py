from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('boards/<int:pk>/',views.board_topics,name='board_topics'),
    path('boards/<int:pk>/new/',views.add_board_topics,name='add_board_topics'),
    path('boards/<int:pk>/topics/<int:topic_pk>/',views.topic_post,name='topic_posts'),
    path('boards/<int:pk>/topics/<int:topic_pk>/reply/',views.posts_reply,name='posts_reply'),
]
