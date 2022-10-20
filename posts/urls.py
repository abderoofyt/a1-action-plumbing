from django.urls import path
from .views import HomeView, PostView, PostCreateView, PostUpdateView, PostDeleteView
from .views import AddLike, AddDislike

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('post/<pk>/<slug:slug>', PostView.as_view(), name='post'),

    path('post/<int:pk>/<slug:slug>/like', AddLike.as_view(), name='like'),
    path('post/<int:pk>/<slug:slug>/dislike', AddDislike.as_view(), name='dislike'),

    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]