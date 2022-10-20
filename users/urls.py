from django.urls import path
from .views import *

urlpatterns = [

    path('register/', register, name='register'), 
    path('dashboard/', dashboard, name='dashboard'), 

    path('login/', user_login, name='login'), 
    path('logout/', user_logout, name='logout'), 

    path('profiles/', profile_list, name='profiles'), 
    path('profiles/<id>/', profile_detail_view, name='profiles'), 

    path('profiles/<id>/update', profile_update_view, name='profile_update_view'), 
    path('profiles/<id>/delete', profile_delete_view, name='profile_delete_view'), 

    path('send_friend_request/<int:userID>/', send_friend_request, name='send friend request'),
    path('accept_friend_request/<int:requestID>/', accept_friend_request, name='accept friend request'),
    
    path('', users_list, name='users'), 
    # path('create/', user_create, name='user_create'),

]