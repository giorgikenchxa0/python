from django.urls import path
from .views import HomeView , about_views ,post_create_views, post_delete_view, random_post_create_view,post_update_view,post_detail_view

urlpatterns = [
 
    path('', HomeView.as_view(), name= "home"),
    path('about/', about_views,  name= "about"),
    path('post/create/',post_create_views, name= "post_create"),
    path("posts/<int:post_id>/delete/", post_delete_view, name="post_delete"),
    path('post/create/random/', random_post_create_view, name= 'post_create_random' ),
    path('posts/<int:pk>/update/', post_update_view, name='post_update'),
    path('posts/<int:pk>/',post_detail_view, name= 'post_detail' ),
    
]
