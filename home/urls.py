from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
<<<<<<< HEAD
=======
    
>>>>>>> b27dab80c583e3bbf1bbd251cacd9adc181b4d37
    path('orders/', views.orders, name='orders'),
    path('orders/<id>/complete/', views.orders_complete, name='orders_complete'),

    path('pricing/<id>/', views.pricing_detail_view, name='pricing_detail_view'), 

]