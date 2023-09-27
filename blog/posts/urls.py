from django.urls import path, include
from .views import *

urlpatterns = [
    path('', PostHome.as_view(), name='home'),
    path('post/<slug:post_slug>/', PostDetail.as_view(), name='post_detail'),
    path('category/<slug:cat_slug>/', PostCategory.as_view(), name='category')
]
