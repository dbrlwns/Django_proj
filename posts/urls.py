from django.urls import path
from posts.views import post_list, add_post, del_post, update_post, add_comment, del_comment, post_detail, like_click

urlpatterns = [
    path('', post_list, name='post_list'),
    path('detail/<int:id>/', post_detail, name='post_detail'),
    path('add_post/', add_post, name='add_post'),
    path('del_post/<int:id>/', del_post, name='del_post'),
    path('update_post/<int:id>/', update_post, name='update_post'),
    path('add_comment/<int:id>/', add_comment, name='add_comment'),
    path('del_comment/<int:id>/', del_comment, name='del_comment'),
    path('like/<int:id>/', like_click, name='like_click'),
]