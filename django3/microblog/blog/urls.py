from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path('post/', index),
    path('post/create', index),
    path('post/delete', index),
]
