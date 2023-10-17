from django.urls import path, include
from . import api

app_name = 'user'

urlpatterns = [
    path('api/list', api.user_list_api, name='userlist'),
    # path('api/user', include('users.url')),
    # path('api/posts/', include('posts.urls')),
]
