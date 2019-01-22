from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
	path('forum/post/<int:id>', views.post, name='post_detail'),
	path('forum/', views.posts, name='post_list'),
	path('forum/new', views.createpost, name="new_post"),

]

