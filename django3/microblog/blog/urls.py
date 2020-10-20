from django.urls import path
from .views import index, posts, create, delete, info

urlpatterns = [
    path('', posts),
    path('post/create', create),
    path('post/delete', delete),
    path('post/search', info),
    path('post/info',   info),
    path('<str:name>',  index)
]
