from urllib import request
from django.urls import path
from . views import AddPostView, DeletePostView, UpdatePostView, home, ArticleDetailView

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/eidt/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
]
