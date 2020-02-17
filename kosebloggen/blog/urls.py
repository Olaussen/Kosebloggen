from .views import PostDetail, PostList, AboutView, ContactView
from django.urls import path

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('/about/', AboutView.as_view(), name="about"),
    path('/contact/', ContactView.as_view(), name="contact"),
]