from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('info/', views.info, name='info'),
    path('profiles/', views.profiles, name='profiles'),
    path('orders/', views.orders, name='orders'),
    path('orders/<id>/complete/', views.orders_complete, name='orders_complete'),

    path('pricing/<id>/', views.pricing_detail_view, name='pricing_detail_view'), 

    path('list/', views.list_view),
    path('create/', views.create_view),
    path('list/<id>/', views.detail_view),
    path('list/<id>/update/', views.update_view),
    path('list/<id>/delete/', views.delete_view),

]